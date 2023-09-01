#!/bin/bash
# Script makes http POST request to a server

curl -s -X POST --data "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1";
