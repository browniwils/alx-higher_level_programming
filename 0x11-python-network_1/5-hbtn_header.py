#!/usr/bin/python3
"""
Send http and print the
X-Request-Id value of the header
"""
from sys import sys
from requests import get


def http_request(url):
    """
    Send a GET request
    and print the X-Request-Id header value
    """
    if url:
        try:
            return get(url).headers.get('X-Request-Id')
        except Exception as e:
            return e


if __name__ == "__main__":
    print(http_request(sys.argv[1]))
