#!/usr/bin/python3
"""
Script send http POST request to
localhost:5000/search_user with
query string and print response in JSON
"""
import sys
from requests import post


def http_request(query_string):
    """
    Send http POST request with questy_string
    """
    resource = "http://0.0.0.0:5000/search_user"
    response = post(resource, data={'q': query_string}).text
    try:
        json_response = eval(response)
        if len(json_response) != 0:
            return "[{}] {}".format(json_response.get('id'), json_response.get('name'))
        return "No result"
    except Exception as e:
        return "Not a valid JSON"


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(http_request(sys.argv[1]))
    else:
        print(http_request(""))
