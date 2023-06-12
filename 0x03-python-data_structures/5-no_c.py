#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for chars in my_string:
        if chars.lower() != 'c':
            new += chars
    return new
