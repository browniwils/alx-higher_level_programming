#!/usr/bin/python3
"""
Send http request and print the response
"""
import sys
from requests import get


def http_request(url):
    """
    Send a request, get the response,
    and handle exceptions
    """
    response = get(url)
    if int(response.status_code) >= 400:
        return ("Error code: {}".format(response.status_code))
    return response.text


if __name__ == "__main__":
    print(http_request(sys.argv[1]))
