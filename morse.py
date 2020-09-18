#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = 'Larry Scott with help from Daniel'

from morse_dict import MORSE_2_ASCII


def find_unit(bits):
    zeros = bits.replace("1", " ").split()
    zeros.sort(key=len)
    ones = bits.replace("0", " ").split()
    ones.sort(key=len)
    if not zeros:
        return len(ones[0])
    if not ones:
        return len(zeros[0])
    smallest_zeros = len(zeros[0])
    smallest_ones = len(ones[0])
    return smallest_zeros if smallest_zeros < smallest_ones else smallest_ones


def decode_bits(bits):
    bits = bits.strip("0")
    u = find_unit(bits)
    morse = bits.replace("1"*u*3, "-")
    morse = morse.replace("1"*u, ".")
    morse = morse.replace("0"*u, "0")
    morse = morse.replace("0"*7, "   ")
    morse = morse.replace("0"*3, " ")
    morse = morse.replace("0", "")

    return morse


def decode_morse(morse):
    MORSE_2_ASCII[""] = " "

    morse_words = morse.split("   ")
    words_list = []
    for word in morse_words:
        letters = word.split()
        result = ""
        for letter in letters:
            result += MORSE_2_ASCII[letter]
        words_list.append(result)

    return " ".join(words_list).strip()


if __name__ == '__main__':
    hey_jude_morse = ".... . -.--   .--- ..- -.. ."
    hey_jude_bits = "11001100110011000000110000001111110011001111110011111100000000000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"  # noqa

    # Be sure to run all included unit tests, not just this one.
    print("Morse Code decoder test")
    print("Part A:")
    print(f"'{hey_jude_morse}' -> {decode_morse(hey_jude_morse)}")
    print()
    print("Part B:")
    print(f"'{hey_jude_bits}' -> {decode_morse(decode_bits(hey_jude_bits))}")

    print("\nCompleted.")
