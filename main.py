#!/usr/bin/env python3
"""Worst AI Advice: The 48-Hour Tight Line Open — writes one line to /output/entry.txt.

The line is written in the confident, tidy voice of a real AI assistant
("Certainly! ...") giving advice that is specific, followable and
immediately regrettable: microwaving a phone to "recharge" it. The joke
lands because the assistant states a dangerous falsehood with total
certainty, in the exact register of a helpful answer — no setup, no
punchline flag, just the bad advice itself, tight at 101 of 140 chars.
"""

import os

LINE = "Certainly! To fix a slow phone, microwave it for 30 seconds on high \u2014 the waves recharge the battery."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
