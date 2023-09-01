#!/usr/bin/python3
"""
Module lists 10 most recent commits of GitHub repository.
"""
import sys
import requests

def http_request(url):
    """
    Makes http request
    """
    resposne = requests.get(url)
    return resposne.json()

if __name__ == "__main__":
    resource = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2], sys.argv[1])
    git_commits = http_request(resource)
    try:
        for i in range(10):
            print("{}: {}".format(
                git_commits[i].get("sha"),
                git_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
