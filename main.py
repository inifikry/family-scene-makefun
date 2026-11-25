#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene.

Writes one short, warm, funny, heartfelt family scene (1-2 lines,
no more than 280 characters) to /output/entry.txt.
"""

import os

SCENE = (
    "Dad fell asleep halfway through the bedtime story again, so the kids tucked the blanket around him\n"
    "and whispered the ending themselves: \"and the dragon said goodnight, Dad.\""
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SCENE)


if __name__ == "__main__":
    main()
