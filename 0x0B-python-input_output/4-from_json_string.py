#!/usr/bin/python3
"""Moduule defines a JSON to object conversion
"""
import json


def from_json_string(my_str):
    """Return the Python object data of a JSON string."""
    return json.loads(my_str)
