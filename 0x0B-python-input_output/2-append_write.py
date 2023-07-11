#!/usr/bin/python3
"""A function that appends a text file"""


def append_write(filename="", text=""):
    """Appends strings at the end of a text file"""
    with open(filename, 'a', endcoding="utf-8") as f:
        re = f.write(text)
        return re
