#!/usr/bin/python3
"""
this script manages error messages with requests package
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    url = argv[1]
    req = requests.get(url)
    code = req.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(req.text)
