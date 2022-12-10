#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    my_list = list(new_dir.keys())

    for i in my_list:
        new_dir[i] *= 2

    return new_dir
