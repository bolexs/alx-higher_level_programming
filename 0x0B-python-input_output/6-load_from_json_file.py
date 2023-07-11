#!/usr/bin/python3
"""A function to read a json file"""
import json


def load_from_json_file(filename):
    """An obj from a json file"""
    with open(filename) as f:
        return json.load(f)
