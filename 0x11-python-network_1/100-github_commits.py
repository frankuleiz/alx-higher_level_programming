#!/usr/bin/python3
"""
A script list 10 commits from the oldest to the newest of the repo
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    repo_name = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)

    resp = requests.get(url)
    commits = resp.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print("{}: {}".format(sha, author_name))
