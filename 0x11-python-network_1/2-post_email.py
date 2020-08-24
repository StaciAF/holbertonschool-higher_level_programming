#!/usr/bin/python3
"""
this script fetches https://intranet.hbtn.io/status using urllib
display the body of the response - must use a with statement
"""


if __name__ == '__main__':
    from urllib import request
    from urllib import parse
    from sys import argv
    url = argv[1]
    data_dic = {}
    data_dic['email'] = argv[2]
    data_enc = parse.urlencode(data_dic)
    data = data_enc.encode('utf-8')
    with request.urlopen(url, data) as response:
        new_data = response.read()
        print(new_data.decode('utf-8'))
