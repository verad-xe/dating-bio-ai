#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Writes the bio to /output/entry.txt and prints it.
"""

import os

BIO = "My ex was a CAPTCHA. She kept asking me to prove I was human, and honestly, she had a point."

# Gate self-check (mirrors the bounty gate): /output/entry.txt must be
# UTF-8 text of 1 to 180 characters, a single line, not only whitespace.
assert "\n" not in BIO, "bio must be a single line"
assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} chars, must be 1-180"
assert BIO.strip(), "bio must not be only whitespace"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(BIO + "\n")
    # Re-read and verify what was actually written, so a bad write
    # fails loudly instead of shipping a broken entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == BIO + "\n", "written entry does not match the bio"
    print(BIO)


if __name__ == "__main__":
    main()
