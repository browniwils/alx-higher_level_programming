#!/usr/bin/python3
""" Module contains one class
"""


class MyList(list):
    """Example subclass of list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints sorted list nicely"""
        print(sorted(self))
