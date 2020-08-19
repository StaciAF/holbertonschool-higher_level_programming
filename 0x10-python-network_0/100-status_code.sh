#!/bin/bash
# this script sends a request then displays only the response status code
curl -s -o /dev/null -I -w "%{http_code}" "$1"
