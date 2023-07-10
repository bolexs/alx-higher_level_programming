#!/usr/bin/python3
"""Defines a function"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attrs to an obj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
