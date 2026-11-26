"""What the Elevator Would Say — one-line entry.

The elevator speaks in its own voice: a tired worker that knows
everyone's routine and has never once been asked how it is doing.
"""

LINE = "Twenty years I've carried this building. Not once has anyone asked how I am — they just press 12 and sigh."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"{len(LINE)} chars: {LINE}")
