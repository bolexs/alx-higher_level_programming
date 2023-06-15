#!/usr/bin/python3
def uniq_add(my_list=[]):
    counter = 0
    for num in set(my_list):
        counter += num
        return counter
