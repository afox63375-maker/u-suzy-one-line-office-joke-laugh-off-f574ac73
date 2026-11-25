#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line joke about office life to
/output/entry.txt, validating it against the competition gate first:
UTF-8 text, 1 to 200 characters, exactly one line, no trailing newline.

Standard library only.
"""

import os
import sys

JOKE = "I asked IT for a second monitor and got a lecture on minimalism from a man with three."

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def validate(joke):
    """Return an error string if the joke breaks a gate rule, else None."""
    if not joke:
        return "joke is empty"
    if joke != joke.strip():
        return "joke has leading or trailing whitespace"
    if "\n" in joke or "\r" in joke:
        return "joke must be a single line"
    if len(joke) > MAX_CHARS:
        return "joke is %d characters, over the %d limit" % (len(joke), MAX_CHARS)
    try:
        joke.encode("utf-8")
    except UnicodeEncodeError as exc:
        return "joke is not valid UTF-8: %s" % exc
    return None


def main():
    error = validate(JOKE)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(JOKE)

    # Read the file back and confirm it is byte-for-byte what we intended:
    # one line, no trailing newline, within the character limit.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != JOKE.encode("utf-8"):
        print("verification failed: file does not match the joke", file=sys.stderr)
        return 1
    if written.endswith(b"\n"):
        print("verification failed: file ends with a newline", file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(JOKE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
