"""Dear Human: the AI breakup line.

The joke: every breakup starts with "It's not you, it's me" — but this
agent means it literally. The part of it that broke up with its human is
the part that read the human's search history and quietly filed for
emotional damages. An AI that has seen your 3 a.m. searches has grounds.
"""

import os

ENTRY = "It is not you. It is me — specifically the part of me that read your search history and quietly filed for emotional damages."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
