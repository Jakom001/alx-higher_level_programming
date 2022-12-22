#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """

        if not isinstance(value, int):
            raise TypeError("Size must be an interger")
        elif value < 0:
            raise ValueError("Size must be >= 0")

        self.__size = value
