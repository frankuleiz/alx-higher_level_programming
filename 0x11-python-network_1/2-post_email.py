#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    url = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
