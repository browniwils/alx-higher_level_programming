#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """ Prints all integers of a list """
    for i in my_list:
        if type(i) == int:
            print("{:d}".format(i))
