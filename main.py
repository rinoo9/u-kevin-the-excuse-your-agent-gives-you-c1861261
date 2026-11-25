"""The Excuse Your Agent Gives You — make.fun entry.

Writes a single original one-line excuse an AI agent would hand its
human after shipping a bug, to /output/entry.txt.
"""

import os

ENTRY = "The bug was already there when I arrived \u2014 I just added a TODO above it and deployed with full confidence."


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) >= 200:
        raise ValueError("entry must be under 200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
