#!/bin/bash
# Script makes a GET request and print response body size to standard output

curl -s "$1" | wc -c

