#!/usr/bin/python3
""" Script takes a URL, sends a request and displays the body of the response """
from sys import argv
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    responses = requests.get(url, auth=HTTPBasicAuth(username, password))
    print(responses.json().get('id'))
