#!/usr/bin/python3
"""
Make http request with an email as payload
and print the response
"""
import sys
from requests import post


def http_request(url, email):
    """
    Send a request and get the response
    """
    try:
        return (post(url, data={"email": email}).text)
    except Exception as error:
        return error


if __name__ == "__main__":
    print(http_request(sys.argv[1], sys.argv[2]))
