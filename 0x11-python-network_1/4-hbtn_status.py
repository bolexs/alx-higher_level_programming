#!/usr/bin/python3
""" Script that fetches a particular URL """
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
