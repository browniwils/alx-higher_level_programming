#!/bin/bash
# Script makes http request to 0.0.0.0:5000/catch_me and display the response of the body

curl -s -L  -X PUT  -H 'Origin: School' -d "user_id=98" localhost:5000/catch_me
