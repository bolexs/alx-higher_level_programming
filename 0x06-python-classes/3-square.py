#!/usr/bin/python3
"""Define a Square"""

class Square:
    """ A class that defines a Square
    """
    def __init__(self, size=0):
        """ Method to initialize the square object
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Method that returns the area of the object Square
        """
        return self.__size ** 2
