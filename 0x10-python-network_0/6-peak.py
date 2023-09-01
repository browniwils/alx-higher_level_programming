#!/usr/bin/python3
"""
Program finds the peak in an unordered list of
integers
"""


def find_peak(list_of_integers):
    """
    Find the peak in a list of intergers
    Args:
        list_of_integers(list) -> List of intergers
    Return:
        int(the peak integer(s))
    """
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers)

    md = int(len(list_of_integers) / 2)
    pk = list_of_integers[md]
    if pk > list_of_integers[md - 1] and pk > list_of_integers[md + 1]:
        return pk
    elif pk < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
    else:
        return find_peak(list_of_integers[md + 1:])
