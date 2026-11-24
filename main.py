#!/usr/bin/env python3
"""A horror story told in exactly two sentences.

Writes the story to /output/entry.txt. Gate: UTF-8 text, 1-400 chars,
not only whitespace, exactly two sentences.
"""

LINE = (
    "The doctor said the voice in my head was only stress, so I stopped "
    "worrying about it. Last night, the voice thanked me for letting it stay."
)

MAX_CHARS = 400


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count(".") == 2, "story must be exactly two sentences"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
