#!/usr/bin/python3
"""A function that returns a JSON obj"""
import json


def to_json_string(my_obj):
    """Return the JSON object"""
    return json.dumps(my_obj)
