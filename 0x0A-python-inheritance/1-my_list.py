#!/usr/bin/python3
"""Defines a MyList Class"""

class MyList(list):
    """Inherit attrs from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
