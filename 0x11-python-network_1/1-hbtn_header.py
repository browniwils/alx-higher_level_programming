#!/usr/bin/python3
"""
Find the value of the X-Request-Id in response
"""
import sys
from urllib import request, error


def http_request(url):
    """
    Send http request and
    get the response headers
    """
    try:
        with request.urlopen(url) as response:
            return response.info()['X-Request-Id']
    except error.URLError as e:
        return e.reason


if __name__ == "__main__":
    print(http_request(sys.argv[1]))
