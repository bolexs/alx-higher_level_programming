#!/usr/bin/python3
"""Function that write to a file"""

def write_file(filename="", text=""):
    """Write a string to text file"""
    with open(filename, "w", encoding="utf-8") as f:
        re = f.write(text)
        return re
