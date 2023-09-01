#!/bin/bash
# Script makes http request to 0.0.0.0:5000/catch_me and display the response of the body
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me