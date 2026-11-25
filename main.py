#!/usr/bin/env python3
"""The Best Meal You Ever Had.

Prints one line about the best meal ever had.
Deterministic: the same line every run, no randomness, no input.
"""

ENTRY = (
    "The best meal I ever had was a $3 nasi goreng at 2 a.m. on a "
    "plastic stool \u2014 no menu, no reservation, just wok fire and a "
    "cook who nodded like we had known each other for years."
)

assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
