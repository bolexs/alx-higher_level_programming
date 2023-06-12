#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    lister = my_list[:]
    if 0 <= idx < length:
        lister[idx] = element

    return new_list
