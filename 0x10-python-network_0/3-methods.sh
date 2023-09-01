#!/bin/bash
# Script makes preflight request to find out http methods the server supports
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-