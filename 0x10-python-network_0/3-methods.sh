#!/bin/bash
# Script makes preflight request to find out http methods the server supports

curl -si -X OPTIONS "$1" | grep "Allow" | cut -d " " -f 2-
