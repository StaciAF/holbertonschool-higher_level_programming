#!/bin/bash
# this script sends a JSON POST request
curl -sH "Content-Type: application/json" "$1" -X POST -d @"$2"
