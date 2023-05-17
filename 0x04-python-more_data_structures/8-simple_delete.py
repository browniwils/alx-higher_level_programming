#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if len(key) < 1:
        return a_dictionary

    del a_dictionary[key] if a_dictionary[key] is not None

    return a_dictionary
