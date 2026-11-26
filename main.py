#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun one-liner entry.

The GPS, in its own voice, defends sending the driver down the wrong road.
Stubborn, never apologetic: the field really does have a road on the 2019 map,
and the GPS would rather update its confidence than its data.
"""
import os

LINE = "That field has a road on the 2019 map. I do not update maps. I update confidence."


def main():
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
