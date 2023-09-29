#!/usr/bin/python3
""" Script takes a URL and an email params, sends a POST request to the URL with an email params, and displays the body of the response"""
from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    values = {'email': email}
    data = parse.urlencode(values).encode('ascii')
    with request.urlopen(url, values=data) as response:
        html = response.read()
        print(html.decode('utf-8'))
