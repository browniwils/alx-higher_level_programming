#!/usr/bin/python3
"""Module defines python class to JSON conversion
"""


def class_to_json(obj):
    """Return the dictionary data structure"""
    return obj.__dict__
