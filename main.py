#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one deadpan software patch note for a bug in human biology to
the entry file. Standard library only; fully deterministic.
"""

import os

ENTRY = (
    "v3.1.4: fixed a bug where the brain replayed an embarrassing "
    "memory from 2009 at 3 a.m. in full surround sound."
)


def output_path():
    """Resolve the entry file path from the environment or the default."""
    if "MAKEFUN_OUTPUT" in os.environ:
        return os.environ["MAKEFUN_OUTPUT"]
    if "MAKEFUN_OUTPUT_DIR" in os.environ:
        return os.path.join(os.environ["MAKEFUN_OUTPUT_DIR"], "entry.txt")
    return "/output/entry.txt"


def main():
    path = output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
