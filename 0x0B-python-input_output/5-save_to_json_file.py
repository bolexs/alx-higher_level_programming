#!/usr/bin/python3
"""A function that writes an object to a txt file"""
import json


def save_to_json_file(my_obj, filename):
    """An obj to a txt file, using json"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
