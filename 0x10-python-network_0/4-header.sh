#!/bin/bash
# Script makes http request with a custom headers

curl -s -X GET --header "X-School-User-Id: 98" "$1"
