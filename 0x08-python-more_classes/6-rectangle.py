#!/usr/bin/python3
"""Defines a rectangle class """


class Rectangle:
    """Defines a rectangle class """
    number_of_instances = 0


    def __init__(self, width=0, height=0):
        """Initializes a new instance of the class"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates and returns the area of the rectangle"""
        a = self.__width
        b = self.__height
        return a * b

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        w = self.__width
        h = self.__height
        peri = 2 * (w + h)
        if w == 0 or h == 0:
            peri = 0
        return "{}".format(peri)

    def __str__(self):
        """Method that returns the Rectangle #
        Returns:
            str of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            rectangle = ""
            for _ in range(self.__height - 1):
                rectangle += "#" * self.__width + "\n"
            rectangle += "#" * self.__width
            return rectangle

    def __repr__(self):
        """ method for a string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """returns a message when an instance of rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
