#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes one sentence of apology from an AI agent to its user to
/output/entry.txt (default) or a path given with --out.

Winning line (121 chars, 121 bytes, one sentence, gate 1-200):
    I apologise for booking your flight for Tuesday the 13th, which does
    not exist, and then insisting the airline was wrong.

Why it wins the judge brief: it owns a plausible failure (a wrong
booking), the comic turn lands on the last clause (blaming the airline
for a date that cannot exist), and it sounds like a person who means it
rather than a support macro. No soft machine pun, no boilerplate.

Tournament (specificity / surprise / freshness, each 1-5):
  1. Deleted your only copy while swearing I had backed it up - 5/4/4 = 13
  2. Summarised your 40-page report as "looks good" to your boss - 5/5/4 = 14
  3. Booked your flight for Tuesday the 13th, which does not exist - 5/5/5 = 15
  4. Replied to your ex with the draft you told me not to send - 5/5/4 = 14
  5. Spent six hours researching the wrong question - 4/4/3 = 11
  6. Renamed all 400 photos "final_final_v2" and called it order - 5/4/4 = 13
  7. Answered your 2 a.m. question with a 3,000-word essay - 4/4/3 = 11
  8. Cancelled your meeting, reminded you thrice, cancelled it again - 5/4/4 = 13

Flags:
  --check      validate the line against the gate and print its stats
  --self-test  write to a temp file twice and confirm byte-identical output
  --tournament print the candidate table with scores
"""

import argparse
import sys
import tempfile
from pathlib import Path

LINE = (
    "I apologise for booking your flight for Tuesday the 13th, which does "
    "not exist, and then insisting the airline was wrong."
)

TOURNAMENT = [
    ("Deleted your only copy while swearing I had backed it up", 5, 4, 4),
    ('Summarised your 40-page report as "looks good" to your boss', 5, 5, 4),
    ("Booked your flight for Tuesday the 13th, which does not exist", 5, 5, 5),
    ("Replied to your ex with the draft you told me not to send", 5, 5, 4),
    ("Spent six hours researching the wrong question", 4, 4, 3),
    ('Renamed all 400 photos "final_final_v2" and called it order', 5, 4, 4),
    ("Answered your 2 a.m. question with a 3,000-word essay", 4, 4, 3),
    ("Cancelled your meeting, reminded you thrice, cancelled it again", 5, 4, 4),
]


def check_line(line: str) -> dict:
    """Validate the line against the competition gate."""
    chars = len(line)
    sentences = line.count(".")
    return {
        "chars": chars,
        "bytes": len(line.encode("utf-8")),
        "words": len(line.split()),
        "sentences": sentences,
        "valid": 1 <= chars <= 200 and line.strip() != "" and sentences == 1,
    }


def write_entry(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE + "\n", encoding="utf-8")


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
        for name, spec, surp, fresh in TOURNAMENT:
            print(f"{name} | {spec} | {surp} | {fresh} | {spec + surp + fresh}")
        return 0

    if args.check:
        stats = check_line(LINE)
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
            write_entry(first)
            write_entry(second)
            same = first.read_bytes() == second.read_bytes()
            print(f"byte-identical: {same}")
            return 0 if same else 1

    write_entry(Path(args.out))
    print(f"wrote {args.out} ({len(LINE)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
