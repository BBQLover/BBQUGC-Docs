# ©︎ BBQ大好き All Rights Reserved.
"""Build all localized MkDocs projects into one static GitHub Pages artifact."""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "site.yml"
SITE_DIRECTORY = ROOT / "site"


def run_checked(command: list[str]) -> None:
    """Run one build step and stop immediately when its output cannot be trusted."""
    subprocess.run(command, cwd=ROOT, check=True)


def load_configuration() -> dict:
    """Load and minimally validate the shared site configuration."""
    configuration = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8"))
    if not configuration.get("domain") or not configuration.get("locales"):
        raise ValueError("site.yml must define a domain and at least one locale.")
    return configuration


def make_alternates(configuration: dict) -> list[dict[str, str]]:
    """Create stable language-selector links shared by every localized build."""
    alternates = []
    for locale, settings in configuration["locales"].items():
        path = settings["path"].strip("/")
        link = f"/{path}/" if path else "/"
        alternates.append({"name": settings["label"], "link": link, "lang": settings["html_language"]})
    return alternates


def make_navigation(navigation: dict) -> list[dict]:
    """Convert nested site navigation into the list form expected by MkDocs."""
    result = []
    for title, target in navigation.items():
        result.append({title: make_navigation(target) if isinstance(target, dict) else target})
    return result


def make_mkdocs_configuration(configuration: dict, locale: str, docs_dir: Path) -> dict:
    """Create one language-specific MkDocs configuration with a shared visual system."""
    settings = configuration["locales"][locale]
    domain = configuration["domain"]
    locale_path = settings["path"].strip("/")
    site_url = f"https://{domain}/{locale_path}/" if locale_path else f"https://{domain}/"
    site_dir = SITE_DIRECTORY / locale_path if locale_path else SITE_DIRECTORY
    return {
        "site_name": settings["site_name"],
        "site_description": settings["description"],
        "site_url": site_url,
        "docs_dir": str(docs_dir),
        "site_dir": str(site_dir),
        "use_directory_urls": True,
        "strict": True,
        "copyright": configuration["copyright"],
        "nav": make_navigation(settings["nav"]),
        "theme": {
            "name": "material",
            "language": settings["theme_language"],
            "font": False,
            "icon": {"logo": "material/book-open-page-variant"},
            "features": [
                "navigation.footer",
                "navigation.instant",
                "navigation.top",
                "content.code.copy",
                "search.highlight",
                "search.suggest",
            ],
            "palette": {"scheme": "default", "primary": "pink", "accent": "purple"},
        },
        "plugins": [{"search": {"lang": [settings["search_language"]]}}],
        "markdown_extensions": [
            "admonition",
            "attr_list",
            "md_in_html",
            {"toc": {"permalink": True}},
            "pymdownx.details",
            "pymdownx.highlight",
            "pymdownx.inlinehilite",
            "pymdownx.superfences",
            "pymdownx.tabbed",
            "pymdownx.tasklist",
        ],
        "extra_css": ["assets/stylesheets/extra.css"],
        "extra": {"alternate": make_alternates(configuration), "generator": False},
    }


def build_locale(configuration: dict, locale: str, temporary_root: Path) -> None:
    """Stage shared assets and build one locale into its final URL path."""
    docs_dir = temporary_root / locale / "docs"
    shutil.copytree(ROOT / "content" / locale, docs_dir)
    shutil.copytree(ROOT / "assets", docs_dir / "assets")
    generated_config = make_mkdocs_configuration(configuration, locale, docs_dir)
    config_path = temporary_root / f"mkdocs.{locale}.yml"
    config_path.write_text(yaml.safe_dump(generated_config, allow_unicode=True, sort_keys=False), encoding="utf-8")
    run_checked([sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(config_path)])
    settings = configuration["locales"][locale]
    locale_path = settings["path"].strip("/")
    built_directory = SITE_DIRECTORY / locale_path if locale_path else SITE_DIRECTORY
    for html_path in built_directory.rglob("*.html"):
        html = html_path.read_text(encoding="utf-8")
        html = re.sub(
            r'<html lang="[^"]+"',
            f'<html lang="{settings["html_language"]}"',
            html,
            count=1,
        )
        html_path.write_text(html, encoding="utf-8")


def write_static_host_files(configuration: dict) -> None:
    """Write the custom-domain and static-host markers into the generated artifact."""
    (SITE_DIRECTORY / "CNAME").write_text(configuration["domain"] + "\n", encoding="utf-8")
    (SITE_DIRECTORY / ".nojekyll").write_text("", encoding="utf-8")


def main() -> int:
    """Validate source, build every locale, and validate the final public artifact."""
    try:
        configuration = load_configuration()
        run_checked([sys.executable, str(ROOT / "scripts" / "validate_locales.py")])
        run_checked([sys.executable, str(ROOT / "scripts" / "check_public_content.py"), str(ROOT)])
        if SITE_DIRECTORY.exists():
            shutil.rmtree(SITE_DIRECTORY)
        with tempfile.TemporaryDirectory(prefix="bbqugc-docs-") as temporary_directory:
            temporary_root = Path(temporary_directory)
            for locale in configuration["locales"]:
                build_locale(configuration, locale, temporary_root)
        write_static_host_files(configuration)
        run_checked([sys.executable, str(ROOT / "scripts" / "check_public_content.py"), str(SITE_DIRECTORY)])
        run_checked([sys.executable, str(ROOT / "scripts" / "verify_site.py")])
    except (OSError, subprocess.CalledProcessError, UnicodeError, ValueError, yaml.YAMLError) as error:
        print(f"Site build failed: {error}", file=sys.stderr)
        return 1
    print(f"Static site built successfully: {SITE_DIRECTORY}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
