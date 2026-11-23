#!/usr/bin/env python3
"""Check a proposed commit message or pull-request title without editing history.

Only the subject line is validated. Co-authored-by trailers are allowed in Glint.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

TYPE = r"(?:feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)"
TITLE = re.compile(rf"^{TYPE}\([a-z0-9][a-z0-9-]*\): [^\s].* \[[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+\]$")


def validate(message: str) -> list[str]:
    lines = message.splitlines()
    if not lines or not lines[0].strip():
        return ["message is empty; add a Conventional Commit subject"]
    if not TITLE.fullmatch(lines[0]):
        return ["subject must match `type(scope): subject [TICKET-ID]` (type: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert; scope required; ticket like [PRJ-001])"]
    return []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--message-file", type=Path, help="commit message file; only the first line is the subject")
    source.add_argument("--title", help="pull-request title")
    args = parser.parse_args()
    if args.title is not None:
        message = args.title
    else:
        try:
            message = args.message_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            print(f"ERROR cannot read commit message file {args.message_file}: {exc}", file=sys.stderr)
            return 2
    errors = validate(message)
    if errors:
        for error in errors:
            print(f"ERROR {error}", file=sys.stderr)
        print("Expected: type(scope): concise subject [TICKET-ID]", file=sys.stderr)
        return 1
    print("PASS: commit/PR convention is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
