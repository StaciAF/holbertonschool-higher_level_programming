#!/usr/bin/python3
"""
this script sends a POST request with url passed as argv using requests package
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    url = argv[1]
    req = requests.post(url, data={'email': argv[2]})
    print(req.text)
