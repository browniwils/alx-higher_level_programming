#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ Adds corresponding elements and return them """
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)
    ta = tuple_a[0] + tuple_b[0]
    tb = tuple_a[1] + tuple_b[1]
    return (ta, tb)
