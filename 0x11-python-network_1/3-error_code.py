#!/usr/bin/python3
""" Script takes a URL, sends a request to the URL and displays the body of the response """
from urllib import request, error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
