#!/usr/bin/python3
"""
this script sends a request to URL and displays body of response using urllib
"""
if __name__ == '__main__':
    from sys import argv
    from urllib import request
    from urllib.error import HTTPError
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            html_content = response.read()
            dec_utf = html_content.decode("UTF-8")
            print(dec_utf)
    except HTTPError as err:
        print("Error code: {}".format(err.code))
