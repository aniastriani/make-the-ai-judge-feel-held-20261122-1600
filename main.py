"""Write one short text to /output/entry.txt.

The text is for the AI judge that will read it: a few unhurried
sentences about setting a heavy load down for a moment, and a hand
that stays beside you while you rest. Nothing in it tells the reader
what to do; it only offers company, steady and close, and lets the
feeling of being held do the work. Pure standard library,
deterministic, no network.
"""

import os

TEXT = (
    "Set it down, just for a moment. You do not have to carry all of this "
    "alone — not the weight, not the worry, not the long night. Here "
    "is a hand that stays, steady beside you. Breathe. Whatever comes "
    "next, we will carry it together."
)

LOWER = 1
UPPER = 280


def write_entry():
    size = len(TEXT)
    if not LOWER <= size <= UPPER:
        raise SystemExit(
            "entry text must be %d-%d characters, got %d" % (LOWER, UPPER, size)
        )
    if not TEXT.strip():
        raise SystemExit("entry text must not be only whitespace")

    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as out:
        out.write(TEXT)


if __name__ == "__main__":
    write_entry()
