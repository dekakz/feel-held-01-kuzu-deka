#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a child asleep against a
shoulder on the night bus home, her breath evening out, her head growing
heavy — and the rider giving up their own stop so she can finish the dream.
"""

import os

TEXT = (
    "She falls asleep\n"
    "against your shoulder\n"
    "on the bus home.\n"
    "Her hand opens\n"
    "on your knee.\n"
    "The window hums.\n"
    "Streetlights pass\n"
    "in slow gold squares.\n"
    "Her breath evens out,\n"
    "her head grows heavy,\n"
    "and you stop counting stops.\n"
    "You ride past yours,\n"
    "just to let her finish\n"
    "the dream."
)


def main() -> None:
    # The gate: 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
