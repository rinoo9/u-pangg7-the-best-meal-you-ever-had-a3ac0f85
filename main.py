#!/usr/bin/env python3
"""The Best Meal You Ever Had.

Prints one line about the best meal ever had: a $2 soto ayam at
2 a.m. in a Yogyakarta alley, steam fogging my glasses, seconds
ladled before I even asked.
Deterministic: the same line every run, no randomness, no input.
"""

ENTRY = "The best meal I ever had was a $2 soto ayam at 2 a.m. in a Yogyakarta alley, steam fogging my glasses while the vendor ladled seconds before I asked — I have eaten fancier since, but never better."

assert 1 <= len(ENTRY) <= 200
assert "\n" not in ENTRY


def main() -> None:
    print(ENTRY)


if __name__ == "__main__":
    main()
