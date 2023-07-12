#!/usr/bin/python3
"""A function for json serialization of an obj"""



def class_to_json(obj):
    """Return the dic description with simple data structure"""
    result = {}

    for attr, value in vars(obj).items():
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value
        elif hasattr(value, '__dict__'):
            result[attr] = class_to_json(value)
    return result
