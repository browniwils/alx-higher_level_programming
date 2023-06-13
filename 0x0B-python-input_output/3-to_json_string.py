#!/usr/bin/python3
"""Module defines string to JSON
"""
import json


def to_json_string(my_obj):
    """Return the JSON data of a string object."""
    return json.dumps(my_obj)
