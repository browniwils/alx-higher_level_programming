#!/usr/bin/python3
"""
Program finds the peak in an unordered list of
integers
"""


def find_peak(list_of_integers):
    """
    Find the peak in an unsorted list of intergers
    `list_of_integers` -> list
    """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    return None
