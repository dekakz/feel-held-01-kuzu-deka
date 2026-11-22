#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a girl on a porch swing
stops pushing with her toes — and the swing keeps going, her father's
foot still on the boards, finding the rhythm for her, while the chains
tick and the yard fills with evening crickets — until she lets her head
fall back and watches the sky swing with her.
"""

import os

TEXT = (
    "She stops pushing\n"
    "with her toes,\n"
    "and the porch swing\n"
    "keeps going.\n"
    "Her father's foot\n"
    "is still on the boards,\n"
    "slow, steady,\n"
    "finding the rhythm for her.\n"
    "The chains tick.\n"
    "The yard fills\n"
    "with evening crickets.\n"
    "She lets her head fall back\n"
    "and watches the sky\n"
    "swing with her."
)


def main() -> None:
    # The gate: 1 to 280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry out of bounds"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
