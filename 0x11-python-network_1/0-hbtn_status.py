#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import urllib.request as request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as r:
        html = r.read()
        print('Body reponse')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))
