#!/usr/bin/python3
"""A function that return an object"""
import json


def from_json_string(my_str):
    """An obj represented by a json string"""
    return json.loads(my_str)
