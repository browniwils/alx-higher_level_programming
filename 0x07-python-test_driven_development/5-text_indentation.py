#!/usr/bin/python3
"""
Defines a text-indentation function
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?', and ':'

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cons = 0
    while cons < len(text) and text[cons] == ' ':
        cons += 1

    while cons < len(text):
        print(text[cons], end="")
        if text[cons] == "\n" or text[cons] in ".?:":
            if text[cons] in ".?:":
                print("\n")
            cons += 1
            while cons < len(text) and text[cons] == ' ':
                cons += 1
            continue
        cons += 1
