#!/bin/bash
# Script makes http request with post method sending JSON data to a server

curl -d "$(cat "$2")" -s -X POST --header "Content-Type: application/json" "$1"
