#!/bin/bash
# Script makes a GET request and print response body size to standard output

curl -sI "$1" | grep -i "Content-Length" | cut -d ":" -f 2
