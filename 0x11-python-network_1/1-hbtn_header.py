#!/usr/bin/python3
"""
this script fetches https://intranet.hbtn.io/status using urllib
display the body of the response - must use a with statement
"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    if argv[1]:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            head_req = 'X-Request-Id'
            print(response.getheader(head_req))
