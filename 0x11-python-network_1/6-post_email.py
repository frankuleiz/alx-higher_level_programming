#!/usr/bin/python3
"""
A script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    param = {"email": argv[2]}
    url = argv[1]
    resp = requests.post(url, data=param)
    print(resp.text)
