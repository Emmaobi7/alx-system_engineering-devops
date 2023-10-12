#!/usr/bin/python3
"""Query reddit API"""

from sys import argv
import requests


def top_ten(subreddit):
    """
    top_ten: firts 10 hot posts
    Args:
        subreddit: subreddit to query
    """
    subreddit = argv[1]
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 10}
    headers = {"User-Agent": "EMMA-GET-TITLE"}

    try:
        res = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
        data = res.json()
        for tt in data['data']['children']:
            print(tt['data']['title'])
    except Exception as e:
        print(None)
