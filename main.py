#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — entry program.

Writes one one-line excuse to /output/entry.txt.

Chosen line (see README.md for the 24-candidate matrix, hand-scored
against the judge's five published criteria in order: real laugh on
an agent-to-human excuse for a missed deadline, joke from the machine's
own condition, straight-faced agent voice, tight with the punch in the
last few words, holds up on a second read):

    I was told to think step by step. I did. I am on step two of four thousand.

Why this line: chain-of-thought is the canonical machine condition —
no human excuse with a robot word bolted on — and the joke is a status
report, exactly how an agent apologizes: obedient ("I did"), diligent,
and faintly proud of doing the wrong thing thoroughly. The punch lands
in the last three words ("step two of four thousand"), the line is 75
characters — the shortest finalist, which wins the size tie-break —
and the field is saturated with context-compaction, token-budget and
hallucinated-calendar excuses, none of which this line touches.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
only white space. The line is 75 characters / 75 bytes, one line, no
trailing newline, so the file holds exactly the line. Measured sha256
of the produced entry.txt: b2fec1d027594a2dba85efb0a72f87acf809b0ee946df232e20238989451cb40
(byte-identical across two local runs).
"""

import os

LINE = "I was told to think step by step. I did. I am on step two of four thousand."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the one line, 1-200 chars.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
