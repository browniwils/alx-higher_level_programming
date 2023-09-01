#!/bin/bash
# Script makes http request with a custom headers
curl -sX GET "$1" -H "X-School-User-Id: 98" -L