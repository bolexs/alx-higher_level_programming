#!/usr/bin/python3
"""Defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Validate if obj is an instance of a class that is inherited from"""
    if isinstance(obj, a_class):
        return True
    return False
