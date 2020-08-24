#!/usr/bin/python3
"""
this script fetches https://intranet.hbtn.io/status using urllib
display the body of the response - must use a with statement
"""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html_content = response.read()
    dec_utf = html_content.decode("UTF-8")
    print("Body response:")
    print("    - type: {}".format(type(html_content)))
    print("    - content: {}".format(html_content))
    print("    - utf8 content: {}".format(dec_utf))
