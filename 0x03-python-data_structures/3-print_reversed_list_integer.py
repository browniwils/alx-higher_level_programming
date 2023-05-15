#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """ Print integer list in reverse """
    for i in reversed(my_list):
        print("{:d}".format(i))
