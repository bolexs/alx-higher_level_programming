#!/usr/bin/python3
""" Script takes a URL, sends the request and displays the value of the X-Request-Id variable found in the header of the response """
from urllib import request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with request.urlopen(url) as response:
        html = response.info()
        print(html['X-Request-Id'])
