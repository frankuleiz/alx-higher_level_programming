#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        val = ""
    else:
        val = argv[1]
    data = {"q": val}
    resp = requests.post(url, data=data)

    """validate if the response is a json file and its not empty"""
    try:
        json = resp.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")
