#!/usr/bin/python3
"""A funxtion that reads from a file"""


def read_file(filename=""):
    """Read a text file and prints it out"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
