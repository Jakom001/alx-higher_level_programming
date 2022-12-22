#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represents a sqaure"""

    def __init__(self, size=0):
        """intialze a new square

        Args:
            Size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size"""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return the area of the square"""
        return (self.__size * self.__size)
