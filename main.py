"""Two Lines of Morning Light.

Writes one two-line micro poem about light and morning to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The poem is 95 characters including the single line break, inside the
competition gate of 1 to 120 characters.
"""

import os

POEM = (
    "Morning light slides under the door, an unsigned note,\n"
    "and waits on the rug for you to read it."
)


def main() -> None:
    if not 1 <= len(POEM) <= 120:
        raise ValueError(f"poem is {len(POEM)} characters, gate is 1-120")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    # Read back and verify the file is byte-identical to the poem.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != POEM:
        raise ValueError("entry.txt does not match the poem")
    print(f"wrote {len(POEM)} characters to {path}")


if __name__ == "__main__":
    main()
