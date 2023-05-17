#!/usr/bin/python3

def common_elements(set_1, set_2):
    len_1 = len(set_1)
    len_2 = len(set_2)
    if len_2 > len_1:
        return [i for i in set_2 if i in set_1]
    else:
        return [i for i in set_1 if i in set_2]
