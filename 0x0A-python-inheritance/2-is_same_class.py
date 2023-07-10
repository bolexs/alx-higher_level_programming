#!/usr/bin/python3
"""Defines a class checking func"""

def is_same_class(obj, a_class):
    """validates if an obj us exactly an instance of a class"""
    if type(obj) == a_class:
        return True
    return False
