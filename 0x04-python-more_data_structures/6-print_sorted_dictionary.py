#!/usr/binpython3

def print_sorted_dictionary(a_dictionary):
    my_list = list(a_dictionary.keys())
    my_list.sort()
    for i in my_list:
        print("{}: {}".format(1, a_dictionary.get(i)))
