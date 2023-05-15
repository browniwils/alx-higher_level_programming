#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ Replace item in a list with element at idx and return new list """
    if idx < 0 or idx > len(my_list) - 1:
        return [i for i in my_list]
    else:
        new_list = []
        for i in range(len(my_list)):
            if i == idx:
                new_list.append(element)
            else:
                new_list.append(my_list[i])
        return new_list
