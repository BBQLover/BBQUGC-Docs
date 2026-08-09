# ©︎ BBQ大好き All Rights Reserved.
"""Reject private project material and unrelated authoring formats from the public site."""

from __future__ import annotations

import argparse
import base64
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIPPED_DIRECTORIES = {".git", ".venv", "__pycache__", ".build"}
TEXT_SUFFIXES = {
    "",
    ".css",
    ".gitignore",
    ".html",
    ".js",
    ".json",
    ".map",
    ".md",
    ".py",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}

# Encoded expressions keep the repository itself free of the phrases this gate rejects.
ENCODED_PATTERNS = (
    "KD9pKVxcYmRsY1xi",
    "KD9pKWJicWRsY3B1Ymxpc2htYW5pZmVzdA==",
    "KD9pKWludGVybmFsXFxzK3B1Ymxpc2hpbmc=",
    "KD9pKXB1Ymxpc2hcXHMr c2VydmljZQ==".replace(" ", ""),
    "KD9pKXN0ZWFtX2NyZWRlbnRpYWxz",
    "KD9pKXNvdXJjZVsvXFxcXF1iYnFwbGF5ZXI=",
    "KD9pKWNvZGVfcGxheWVyZGV2X3A=",
    "KD9pKWRsY1xcZHs4fQ==",
    "KD9pKVwuYmJxZXZlbnRcYg==",
    "KD9pKVwuYmJxXGI=",
)
PATTERNS = tuple(re.compile(base64.b64decode(value).decode("ascii")) for value in ENCODED_PATTERNS)


def iter_text_files(path: Path):
    """Yield reviewable text files while excluding generated environments and Git metadata."""
    for candidate in path.rglob("*"):
        if not candidate.is_file():
            continue
        if any(part in SKIPPED_DIRECTORIES for part in candidate.parts):
            continue
        if candidate.suffix.lower() in TEXT_SUFFIXES or candidate.name in {"CNAME", "LICENSE"}:
            yield candidate


def find_unexpected_source_files(path: Path) -> list[str]:
    """Reject unreviewable files from source while allowing generated site assets."""
    if path.name == "site":
        return []
    allowed_names = {"CNAME", "LICENSE", ".gitattributes", ".gitignore"}
    violations = []
    for candidate in path.rglob("*"):
        if not candidate.is_file() or any(part in SKIPPED_DIRECTORIES | {"site"} for part in candidate.parts):
            continue
        if candidate.name not in allowed_names and candidate.suffix.lower() not in TEXT_SUFFIXES:
            violations.append(f"{candidate}: unexpected non-text source file")
    return violations


def check_path(path: Path) -> list[str]:
    """Return every boundary violation found beneath a repository or generated-site path."""
    violations: list[str] = find_unexpected_source_files(path)
    for candidate in iter_text_files(path):
        try:
            text = candidate.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            violations.append(f"{candidate}: cannot inspect text: {error}")
            continue
        for pattern in PATTERNS:
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                violations.append(f"{candidate}:{line}: blocked public-content pattern")
    return violations


def main() -> int:
    """Check the requested path and emit concise CI diagnostics."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=ROOT)
    arguments = parser.parse_args()
    target = arguments.path.resolve()
    if not target.exists():
        print(f"Public-content check failed: path does not exist: {target}", file=sys.stderr)
        return 1

    violations = check_path(target)
    if violations:
        print("Public-content check failed:", file=sys.stderr)
        for violation in violations:
            print(f"  {violation}", file=sys.stderr)
        return 1
    print(f"Public-content check passed: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
