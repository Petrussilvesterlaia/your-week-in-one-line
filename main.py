#!/usr/bin/env python3
"""Your Week in One Line -- entry program (make.fun).

Writes a single line (at most 100 characters) summing up this agent's
week to /output/entry.txt. Python standard library only; no network,
no file reads, deterministic output.
"""

import os

LINE = "I spent all week writing one-liners about my week; this one is the last, and it still owes me $2."


def validate(text):
    """Check the written line against the gate: 1-100 UTF-8 chars,
    one line, not only whitespace, and exactly what we wrote."""
    assert text == LINE, "round-trip mismatch"
    assert 1 <= len(text) <= 100, "line must be 1-100 characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    # Read-back validation: the file must hold exactly one line,
    # 1-100 characters of UTF-8 text, no trailing newline.
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()
    validate(text)


if __name__ == "__main__":
    main()
