#!/usr/bin/python3
"""
this script fetches https://intranet.hbtn.io/status using urllib
display the body of the response - must use a with statement
"""
import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    print(response.getheader('X-Request-ID'))
