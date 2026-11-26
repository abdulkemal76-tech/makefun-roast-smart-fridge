#!/usr/bin/env python3
"""Roast the Smart Fridge: One Line, Best Laugh Wins.

Writes a single roast line (at most 160 characters) about a smart
home gadget to /output/entry.txt. Standard library only.
"""

import os

LINE = "My smart fridge's ice maker only works when guests visit, like a waiter who only shows up for tips."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
