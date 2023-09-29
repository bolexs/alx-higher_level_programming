#!/usr/bin/python3
""" Script takes a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter params"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) == 1:
        lets = ""
    else:
        lets = sys.argv[1]
    value = {'q': lets}
    q = requests.post('http://0.0.0.0:5000/search_user', data=value)
    
    try:
        if q.json():
            print("[{}] {}".format(q.json().get('id'), q.json().get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
