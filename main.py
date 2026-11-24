"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence (at most 220 characters) pitching a
ridiculous invention that fixes a tiny everyday annoyance, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Pure Python standard library. No network, no model calls.
"""

import os

ENTRY = (
    "The Apology Toaster: a toaster that files a formal written complaint "
    "every time you burn the bread, then refuses to pop up until you "
    "apologise in writing."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 220, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1, "entry must be exactly one sentence"
    # One sentence means exactly one terminal full stop and no newlines:
    # a stray line break would split the pitch into two lines on the card.
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip(), "entry must be a single trimmed line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
