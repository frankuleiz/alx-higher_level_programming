#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    for list in my_list:
        print("{:d}".format(my_list.reverse))
        if not my_list:
            return None
