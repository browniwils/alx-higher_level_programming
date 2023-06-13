#!/usr/bin/python3
"""Module defines a text file-reading function
"""


def read_file(filename=""):
    """Print contents of utf-8 characters"""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
