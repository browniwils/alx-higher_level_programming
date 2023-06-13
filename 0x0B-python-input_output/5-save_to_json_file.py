#!/usr/bin/python3
"""Module defines a JSON content writing to file
"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object dta to a text file using JSON format."""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
