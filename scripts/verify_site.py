# ©︎ BBQ大好き All Rights Reserved.
"""Verify routes, language metadata, links, and static-host markers in the built site."""

from __future__ import annotations

import html.parser
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "site.yml"
SITE_DIRECTORY = ROOT / "site"
SERVER_SIDE_SUFFIXES = {".asp", ".aspx", ".cgi", ".jsp", ".php"}


class ReferenceParser(html.parser.HTMLParser):
    """Collect navigational and asset references from one generated HTML document."""

    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        """Capture href and src values without interpreting unrelated element attributes."""
        for name, value in attributes:
            if name in {"href", "src"} and value:
                self.references.append(value)


def resolve_reference(document: Path, reference: str, domain: str) -> Path | None:
    """Resolve one local reference to its expected artifact path, or ignore external schemes."""
    parsed = urlparse(reference)
    if parsed.scheme in {"data", "mailto", "tel"}:
        return None
    if parsed.scheme in {"http", "https"}:
        if parsed.netloc != domain:
            return None
        raw_path = parsed.path
    elif parsed.netloc:
        return None
    else:
        raw_path = parsed.path
    if not raw_path:
        return None

    decoded = unquote(raw_path)
    if decoded.startswith("/"):
        target = SITE_DIRECTORY / decoded.lstrip("/")
    else:
        target = document.parent / decoded
    target = target.resolve()
    try:
        target.relative_to(SITE_DIRECTORY.resolve())
    except ValueError as error:
        raise ValueError(f"{document} references a path outside the site: {reference}") from error
    if target.suffix == "" or decoded.endswith("/"):
        target /= "index.html"
    return target


def expected_page_path(locale_path: str, source_page: str) -> Path:
    """Map one Markdown navigation target to its generated directory URL."""
    base = SITE_DIRECTORY / locale_path if locale_path else SITE_DIRECTORY
    if source_page == "index.md":
        return base / "index.html"
    return base / Path(source_page).stem / "index.html"


def navigation_pages(navigation: dict) -> list[str]:
    """Return every page target from a possibly grouped navigation mapping."""
    pages = []
    for target in navigation.values():
        pages.extend(navigation_pages(target) if isinstance(target, dict) else [target])
    return pages


def verify_site() -> None:
    """Validate the complete artifact against locale and static-host configuration."""
    configuration = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    domain = configuration["domain"]
    if (SITE_DIRECTORY / "CNAME").read_text(encoding="utf-8").strip() != domain:
        raise ValueError("Generated CNAME does not match config/site.yml.")
    if not (SITE_DIRECTORY / ".nojekyll").is_file():
        raise ValueError("Generated site is missing .nojekyll.")

    expected_hreflangs = {settings["html_language"] for settings in configuration["locales"].values()}
    expected_pages: list[tuple[Path, str]] = []
    for settings in configuration["locales"].values():
        for source_page in navigation_pages(settings["nav"]):
            expected_pages.append(
                (expected_page_path(settings["path"].strip("/"), source_page), settings["html_language"])
            )

    missing = [str(path) for path, _ in expected_pages if not path.is_file()]
    if missing:
        raise ValueError(f"Generated locale routes are missing: {missing}")

    for page, html_language in expected_pages:
        text = page.read_text(encoding="utf-8")
        if f'<html lang="{html_language}"' not in text:
            raise ValueError(f"{page} does not declare html language '{html_language}'.")
        actual_hreflangs = {
            value.split('"', 1)[0]
            for value in text.split('hreflang="')[1:]
        }
        if actual_hreflangs != expected_hreflangs:
            raise ValueError(f"{page} has incomplete alternate-language metadata.")

    failures: list[str] = []
    for candidate in SITE_DIRECTORY.rglob("*"):
        if candidate.is_file() and candidate.suffix.lower() in SERVER_SIDE_SUFFIXES:
            failures.append(f"server-side artifact is not allowed: {candidate}")
        if not candidate.is_file() or candidate.suffix.lower() != ".html":
            continue
        parser = ReferenceParser()
        parser.feed(candidate.read_text(encoding="utf-8"))
        for reference in parser.references:
            target = resolve_reference(candidate, reference, domain)
            if target is not None and not target.exists():
                failures.append(f"{candidate}: missing target for '{reference}'")
    if failures:
        raise ValueError("Generated-site verification errors:\n  " + "\n  ".join(failures))


def main() -> int:
    """Run artifact verification and return a process-friendly status code."""
    try:
        verify_site()
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        print(f"Generated-site verification failed: {error}", file=sys.stderr)
        return 1
    print("Generated-site verification passed for all routes, locales, and links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
