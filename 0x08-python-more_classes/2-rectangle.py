#!/usr/bin/python
"""Define a class rectangle"""


class Rectangle:
    """Represent a class"""

    def __init__(self, width=0, height=0):
        """instantiation of a class

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle"
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """set the width of the rectangele"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer ")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer ")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)
