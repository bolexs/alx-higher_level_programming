#!/usr/bin/python3
"""Defines a rectangle class """


class Rectangle:
    """Defines a rectangle class """
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets/defines the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets/defines the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
