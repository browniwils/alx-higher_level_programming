#!/bin/bash
# Script makes http request with post method sending JSON data to a server
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"