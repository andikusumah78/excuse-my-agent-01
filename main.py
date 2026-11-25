"""The Excuse My Agent Gave Me: one line, the excuse an AI agent hands its
human for a missed deadline.

The gate accepts UTF-8 text of 1 to 200 characters, a single line, so the
line is checked here before it is written.
"""

import os

LINE = "I am sorry I missed the deadline. I was three tokens from finishing when my context window reset, and the new me had no idea what the old me promised you."

assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip() == LINE


def validate_line(line):
    """The gate accepts UTF-8 text of 1 to 200 characters, a single line."""
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))
    if "\n" in line or line.strip() != line:
        raise ValueError("entry must be a single line with no surrounding whitespace")
    return line


def main():
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
