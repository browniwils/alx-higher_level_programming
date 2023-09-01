#!/bin/bash
# Script sends http request and display the body of the response

curl -sL --fail -X GET "$1";
