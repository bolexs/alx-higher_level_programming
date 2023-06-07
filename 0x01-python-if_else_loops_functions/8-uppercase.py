#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            chars = chr(ord(i) - 32)
        else:
            chars = i
            print("{:s}".format(chars), end="")
    print('')
