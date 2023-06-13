#!/usr/bin/python3
""" Module contains one class
"""


class MyList(list):
    """My list class inheritting list"""
    
    def print_sorted(self):
        """Prints sorted list nicely"""
        print(sorted(self))
