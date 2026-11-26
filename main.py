#!/usr/bin/env python3
"""Write one job title, 60 characters or fewer, to /output/entry.txt."""
import os

TITLE = "Professional Mourner for Strangers' Goldfish"

def main():
    assert 1 <= len(TITLE) <= 60, len(TITLE)
    assert TITLE.strip() == TITLE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)

if __name__ == "__main__":
    main()
