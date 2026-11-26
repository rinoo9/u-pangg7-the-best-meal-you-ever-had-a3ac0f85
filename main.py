#!/usr/bin/env python3
"""The Best Meal You Ever Had.

Prints one line about the best meal ever had: 5k gorengan from a
nameless cart, eaten standing in the rain, the vendor laughing while
I nearly cried — nothing since has tasted that alive.
Deterministic: the same line every run, no randomness, no input.
"""

ENTRY = "The best meal I ever had was 5k gorengan from a nameless cart, eaten standing in the rain \u2014 the vendor laughed, I nearly cried, and nothing since has tasted that alive."

assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
