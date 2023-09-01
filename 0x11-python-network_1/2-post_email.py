#!/usr/bin/python3
"""
Send http request with an email and print the response
"""
import sys
from urllib import request, error, parse


def http_request(url, email):
    """
    Send a request with email payload and
    get the response headers
    """
    data = parse.urlencode({"email": email}).encode('utf-8')
    http_request = request.Request(url, data, method="POST")
    try:
        with request.urlopen(http_request) as response:
            return response.read().decode("utf-8")
    except error.URLError as e:
        return e.reason


if __name__ == "__main__":
    print(http_request(sys.argv[1], sys.argv[2]))
