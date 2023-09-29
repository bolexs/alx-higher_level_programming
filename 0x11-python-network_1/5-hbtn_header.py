#!/usr/bin/python3
""" Script takes a URL, sends a request and displays the value of the X-Request-Id variable found in the header"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
