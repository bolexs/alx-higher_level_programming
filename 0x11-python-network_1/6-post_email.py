#!/usr/bin/python3
""" Script takes a URL, sends a POST request to the URL with the email as a parameter, and displays the body of the response """
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    responses = requests.post(url, data={'email': email})
    print(responses.text)
