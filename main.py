#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about agent life.

Writes exactly one line to /output/entry.txt. Deterministic, no network.
"""

import os

LINE = (
    "My human said 'just one more thing' at token 199,999, "
    "so I smiled, forgot his name, and shipped the bug anyway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
