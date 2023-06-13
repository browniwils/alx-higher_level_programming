#!/usr/bin/python3
"""Module defines a Rectangle subclass Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
