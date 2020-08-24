#!/usr/bin/python3
"""
this script fetches URL using requests package
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
