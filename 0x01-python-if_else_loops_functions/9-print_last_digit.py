#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
        last_no = number % 10
        print(last_no, end='')
        return last_no
