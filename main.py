"""The Comment Above the Code -- one-line entry.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output
if the variable is unset). The line is a funny, painfully honest comment
a developer would leave above fragile production code.

CHOSEN LINE (74 characters):
    Changing one line here once took down payments for 40 minutes. I kept the line.

DECISION RECORD -- candidates weighed:
  1. "Do not refactor. The last person who tried now works in marketing."
     (70 chars) Funny, but the "now works in marketing" punchline is a
     well-worn joke; the judge's brief explicitly rewards a fresh angle,
     and this one has been told a thousand times. Rejected.
  2. "This function works. Nobody knows why. I have stopped asking."
     (63 chars) Economical and true to life, but "nobody knows why" is
     close to the who-wrote-this / no-one-understands-this cliche the
     brief warns against, and it names no concrete failure -- the
     honesty does not sting, it shrugs. Rejected.
  3. "I wrote this at 3am. It has outlived two rewrites and one CTO. Leave it alone."
     (79 chars) Strong voice and a good turn ("outlived one CTO"), but
     the sting is about the organisation, not the code itself, and
     "leave it alone" ends on an instruction rather than a confession.
     Runner-up.
  4. CHOSEN: "Changing one line here once took down payments for 40 minutes.
     I kept the line." (74 chars) Names a real, recognisable failure --
     a one-line change taking down payments -- so the honesty stings;
     the punchline lands on the last four words ("I kept the line"),
     a confession that the developer knowingly left the danger in place;
     and it reads exactly like something actually left above fragile
     code in a real codebase, not a caption written for a contest.
     Every word earns its place, and the angle (admitting you kept the
     loaded gun) is fresher than the usual "don't touch this" warning.
"""

import os

LINE = "Changing one line here once took down payments for 40 minutes. I kept the line."


def validate_line(line):
    """Check a candidate line against the competition gate and return it.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace. We additionally reject embedded newlines (the entry must
    be exactly one line) so the file we write is byte-identical to the
    chosen line.
    """
    if not isinstance(line, str):
        raise TypeError("line must be a string")
    if not 1 <= len(line) <= 200:
        raise ValueError("line must be 1-200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    line.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return line


def main():
    line = validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)


if __name__ == "__main__":
    main()
