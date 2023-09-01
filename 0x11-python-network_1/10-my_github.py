#!/usr/bin/python3
"""
Module print github id
"""
import sys
from requests import get
from requests.auth import HTTPBasicAuth


def http_request(username, tokken):
    """
    Make http request for GitHub ID
    """
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer {}".format(tokken),
        "User-Agent": ""
    }
    auth = HTTPBasicAuth(username, tokken)
    response = get("https://api.github.com/user", headers=headers, auth=auth)
    return response.json().get('id')


if __name__ == "__main__":
    get_github_id = http_request(sys.argv[1], sys.argv[2])
    print(get_github_id)
