#!/usr/bin/python3

def no_c(my_string):
    """ Remove character 'c' from string """
    stri = []
    for s in my_string:
        if s.lower() != 'c':
            stri.append(s)
    return "".join(stri)
