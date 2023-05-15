#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ Print integer list in reverse """
    if not my_list:
        pass
    else:
        for i in reversed(my_list):
            print("{:d}".format(i))
