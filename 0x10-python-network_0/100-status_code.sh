#!/bin/bash
# Script makes http request and display only the status code of the response

curl -o /dev/null -sIw "%{http_code}" "$1"
