#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    s = sorted(a_dictionary.keys())
    for key in s:
        print("{}: {}".format(key, a_dictionary[key]))
