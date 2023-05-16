#!/usr/bin/python3

def max_integer(my_list=[]):
    """ Finds maximum integer in list """
    if len(my_list) < 1:
        return None
    max_int = 0
    for i in range(len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return max_int
