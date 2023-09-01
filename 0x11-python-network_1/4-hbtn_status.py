#!/usr/bin/python3
"""
Send http request and print the response
"""
from requests import get


def http_request(url='https://alx-intranet.hbtn.io/status'):
    """
    Send a GET request and print the reponse
    """
    response = get(url)
    print("Body response:")
    print("\t- type: {}".format(str(response).__class__))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    http_request()
