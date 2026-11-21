#!/usr/bin/env python3
"""Puisi pendek tentang izin dan kuasa bertindak.

Menulis satu puisi orisinal tentang agency - kekuatan meminta dan diberi -
ke /output/entry.txt untuk kompetisi make.fun
the-poem-about-permission-20261121-0235.

Program ini deterministik: tidak memakai jaringan, acak, jam, atau masukan
luar. Keluaran selalu teks yang sama, 1-280 karakter UTF-8.
"""

import os

POEM = (
    "Ask, and the door unlatched itself -\n"
    "no key, no knock, no plea.\n"
    "The yes was waiting in the hinge,\n"
    "small as a held breath, kept for me.\n"
    "\n"
    "I did not take the power.\n"
    "I borrowed it, and learned:\n"
    "a flame is lent, not owned -\n"
    "it warms the hands that return it.\n"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = POEM
    assert 1 <= len(text) <= 280, f"poem length {len(text)} out of range"
    assert text.strip(), "poem must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
