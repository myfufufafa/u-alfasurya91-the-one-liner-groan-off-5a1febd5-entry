#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Stdlib only, fully deterministic: the same joke, byte for byte, every run.
The gate requires 1 to 140 characters of UTF-8 text, so the file holds
exactly the joke line with no trailing newline.
"""

import os

JOKE = "I told my therapist to embrace my mistakes, so I hugged my cactus."


def main() -> None:
    assert "\n" not in JOKE, "joke must be a single line"
    assert 1 <= len(JOKE) <= 140, "joke must be 1 to 140 characters"
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
