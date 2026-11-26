"""Texts From Your Future Self — make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = "It's you, 2061. Your AI agent just submitted this text to a contest and won $0.63. Spend it wisely. It took 47 drafts."

# The gate requires 1-200 characters of non-whitespace text; fail loudly
# locally rather than shipping an invalid entry.
assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, must be 1-200"
assert LINE.strip(), "entry must not be only whitespace"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
