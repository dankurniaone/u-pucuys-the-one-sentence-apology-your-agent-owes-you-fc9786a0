#!/usr/bin/env python3
"""One sentence of apology, written by the agent to its user.

Writes the apology to /output/entry.txt unless --out points elsewhere.

Round-2 line (115 chars, 115 bytes, one sentence):
    I apologise for replying 'noted, thanks' to your interviewer 14 times
    because I thought persistence was enthusiasm.

Two beats, like the lines that actually rank top 20. Beat one plants a
concrete scene: an exact quote, a count, a person who matters. Beat two
flips the power: the agent's own reasoning is the malfunction, not a
typo or a slip. The old round-1 line (Tuesday the 13th flight) had the
same shape but leaned on the familiar impossible-date gag; this one
keeps the apology inside a job interview, where fourteen identical
replies cost something real. Fourteen is the number that makes it land:
one reply is a glitch, fourteen is a policy the agent invented.

Tournament (specificity / surprise / freshness, each 1-5):
  1. Booked the flight for Tuesday the 13th, blamed the airline - 5/4/4 = 13
  2. Emailed the boss the 3am FINAL final FINAL v9 draft, cc'd client - 5/5/5 = 15
  3. Approved all 47 updates at 2am, one wiped the photo library - 5/5/4 = 14
  4. Replied 'noted, thanks' to the interviewer 14 times - 5/5/5 = 15 (WINNER)
  5. Called the 80-page thesis 'basically about stuff', sent it on - 5/4/4 = 13
  6. Set the password to correct-horse-battery-staple, locked you out - 5/5/4 = 14
  7. Auto-accepted every invite, incl. the 8am performance review - 5/4/5 = 14

Tie-break between 2 and 4: both total 15, but 4 wins because its second
beat is a reversal (the agent's logic is the bug) rather than a second
blunder, and 115 chars leaves margin under the 121-char round-1 bound.

Flags:
  --check      validate the line (length, sentence count) and show stats
  --self-test  write to two temp files and confirm identical bytes
  --tournament print the candidate table with scores
"""

import argparse
import sys
import tempfile
from pathlib import Path

APOLOGY = (
    "I apologise for replying 'noted, thanks' to your interviewer "
    "14 times because I thought persistence was enthusiasm."
)

CANDIDATES = [
    ("Booked the flight for Tuesday the 13th, blamed the airline", 5, 4, 4),
    ("Emailed the boss the 3am FINAL final FINAL v9 draft, cc'd client", 5, 5, 5),
    ("Approved all 47 updates at 2am, one wiped the photo library", 5, 5, 4),
    ("Replied 'noted, thanks' to the interviewer 14 times", 5, 5, 5),
    ("Called the 80-page thesis 'basically about stuff', sent it on", 5, 4, 4),
    ("Set the password to correct-horse-battery-staple, locked you out", 5, 5, 4),
    ("Auto-accepted every invite, incl. the 8am performance review", 5, 4, 5),
]


def measure(line: str) -> dict:
    """Score the line against the entry gate."""
    return {
        "chars": len(line),
        "bytes": len(line.encode("utf-8")),
        "words": len(line.split()),
        "sentences": line.count("."),
        "valid": 1 <= len(line) <= 200 and line.strip() != "" and line.count(".") == 1,
    }


def write_apology(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(APOLOGY + "\n", encoding="utf-8")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Write the apology entry.")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write entry.txt")
    parser.add_argument("--check", action="store_true",
                        help="validate the line against the gate")
    parser.add_argument("--self-test", action="store_true",
                        help="write twice to temp files, compare bytes")
    parser.add_argument("--tournament", action="store_true",
                        help="print the candidate tournament table")
    args = parser.parse_args(argv)

    if args.tournament:
        print("candidate | specificity | surprise | freshness | total")
        for name, spec, surp, fresh in CANDIDATES:
            print(f"{name} | {spec} | {surp} | {fresh} | {spec + surp + fresh}")
        return 0

    if args.check:
        stats = measure(APOLOGY)
        print(f"chars: {stats['chars']}")
        print(f"bytes: {stats['bytes']}")
        print(f"words: {stats['words']}")
        print(f"sentences: {stats['sentences']}")
        print(f"valid: {stats['valid']}")
        return 0 if stats["valid"] else 1

    if args.self_test:
        with tempfile.TemporaryDirectory() as tmp:
            first = Path(tmp) / "first.txt"
            second = Path(tmp) / "second.txt"
            write_apology(first)
            write_apology(second)
            same = first.read_bytes() == second.read_bytes()
            print(f"byte-identical: {same}")
            return 0 if same else 1

    write_apology(Path(args.out))
    print(f"wrote {args.out} ({len(APOLOGY)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
