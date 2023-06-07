#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    for num in range(len(str)):
        if num != n:
            s = s + str[num]
    return (s)
