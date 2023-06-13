#!/usr/bin/python3
"""Module defines JSON file content reading
"""
import json


def load_from_json_file(filename):
    """Make python object from a JSON data"""
    with open(filename) as file:
        return json.load(file)
