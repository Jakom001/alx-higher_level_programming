#!/usr/bin/python3

"""Define a ``class Square"""


class Square:
    """Represents the class square"""

    def __init__(self, size=0):
        """Initialize the size

        Args:
            Size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an interger")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        self.__size = value

    def area(self):
        """The area of the square"""
