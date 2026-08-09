# ©︎ BBQ大好き All Rights Reserved.
"""Validate that every published locale has the same page set and source revision."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "site.yml"
REVISION_PATTERN = re.compile(r"<!--\s*source-revision:\s*(\d+)\s*-->")


def load_configuration() -> dict:
    """Load the site configuration or fail with an actionable validation message."""
    try:
        return yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise ValueError(f"Cannot read {CONFIG_PATH}: {error}") from error


def validate_page(path: Path) -> int:
    """Return the declared source revision after checking basic page structure."""
    text = path.read_text(encoding="utf-8")
    revision = REVISION_PATTERN.search(text)
    if not revision:
        raise ValueError(f"{path} is missing '<!-- source-revision: N -->'.")
    if len(re.findall(r"^#\s+\S", text, flags=re.MULTILINE)) != 1:
        raise ValueError(f"{path} must contain exactly one level-one heading.")
    return int(revision.group(1))


def navigation_pages(navigation: dict) -> list[str]:
    """Return page targets from navigation groups in display order."""
    pages = []
    for target in navigation.values():
        pages.extend(navigation_pages(target) if isinstance(target, dict) else [target])
    return pages


def validate_locales() -> None:
    """Enforce identical navigation targets and matching revisions in every locale."""
    configuration = load_configuration()
    locales = configuration.get("locales", {})
    default_locale = configuration.get("default_locale")
    if default_locale not in locales:
        raise ValueError("default_locale must identify one configured locale.")

    default_pages = navigation_pages(locales[default_locale].get("nav", {}))
    if not default_pages:
        raise ValueError("The default locale must define at least one navigation page.")

    expected_files = set(default_pages)
    source_revisions: dict[str, int] = {}
    for page in default_pages:
        source_revisions[page] = validate_page(ROOT / "content" / default_locale / page)

    for locale, settings in locales.items():
        locale_pages = navigation_pages(settings.get("nav", {}))
        if set(locale_pages) != expected_files:
            raise ValueError(f"Locale '{locale}' navigation does not match the default page set.")

        actual_files = {path.name for path in (ROOT / "content" / locale).glob("*.md")}
        if actual_files != expected_files:
            raise ValueError(
                f"Locale '{locale}' files differ from navigation: "
                f"missing={sorted(expected_files - actual_files)}, "
                f"extra={sorted(actual_files - expected_files)}"
            )

        for page in locale_pages:
            revision = validate_page(ROOT / "content" / locale / page)
            if revision != source_revisions[page]:
                raise ValueError(
                    f"Locale '{locale}' page '{page}' is revision {revision}; "
                    f"expected {source_revisions[page]}."
                )


def main() -> int:
    """Run locale validation and return a process-friendly status code."""
    try:
        validate_locales()
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Locale validation failed: {error}", file=sys.stderr)
        return 1
    print("Locale validation passed for en, ja, zhs, and zht.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
