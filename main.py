"""Entry for The Robot Vacuum's Best Excuse: writes the excuse to /output/entry.txt."""

import os

TEXT = "I didn't skip the living room — the cat claimed it, and I respect her laws. Also, I ate one sock and I am prepared to discuss terms."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
