#!/bin/bash
# Script makes http POST request to a server
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD" -L