#!/usr/bin/python3
"""
Send http request and print the response
"""
import sys
from urllib import request, error


def http_request(url):
    """
    Send a request, get the response,
    and handle exceptions
    """
    try:
        with request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except error.HTTPError as e:
        return "Error code: {}".format(e.code)


if __name__ == "__main__":
    print(http_request(sys.argv[1]))
