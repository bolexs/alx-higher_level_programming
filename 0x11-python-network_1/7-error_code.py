#!/usr/bin/python3
""" Script takes a URL, sends a request and displays the body of the response """

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    responses = requests.get(url)
    if responses.status_code >= 400:
        print("Error code: {}".format(responses.status_code))
    else:
        print(responses.text)
