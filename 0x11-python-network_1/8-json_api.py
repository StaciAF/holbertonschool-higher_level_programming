#!/usr/bin/python3
"""
this script uses a POST request with parameters
"""
if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'http://0.0.0.0:5000/search_user'
    if argv[1]:
        payload = {'q': argv[1]}
    else:
        payload = {'q': ""}
    try:
        req = requests.post(url, data=payload)
        json_resp = req.json()
        if json_resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_resp['id'], json_resp['name']))
    except ValueError as e:
        print("Not a valid JSON")
