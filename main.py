"""Office joke entry for make.fun.

Writes one single-line office joke to /output/entry.txt (program/v1).
The joke is a fixed string: the program is deterministic by construction.
"""

import os

JOKE = (
    "I filed an IT ticket titled 'computer slow' and IT closed it as "
    "'user slow,' which is the most honest performance review I have "
    "ever received."
)


def resolve_output_path():
    """Where the harness expects the artifact: $MAKEFUN_OUTPUT_DIR, else /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def validate(text):
    """Mirror the sealed gate: 1-200 characters, one line, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if text != text.strip() or "\n" in text or "\r" in text:
        raise ValueError("entry must be a single unpadded line")
    return text


def main():
    path = resolve_output_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validate(JOKE))


if __name__ == "__main__":
    main()
