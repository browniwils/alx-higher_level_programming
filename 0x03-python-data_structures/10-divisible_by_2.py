#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    my_list_bool = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            my_list_bool[i] = True
        else:
            my_list_bool[i] = False

    return my_list_bool
