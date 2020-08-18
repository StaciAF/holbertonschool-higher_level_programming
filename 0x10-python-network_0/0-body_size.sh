#!/bin/bash
# this script sends request to display content length
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
