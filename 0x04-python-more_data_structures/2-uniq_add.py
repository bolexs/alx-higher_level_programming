#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_list = set(my_list)
    num = 0
    for i in uni_list:
        num += i
        return num
