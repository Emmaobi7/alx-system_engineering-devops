#!/usr/bin/python3
"""query reddit API"""

from sys import argv
import requests


def number_of_subscribers(subreddit):
    """
    number_of_subcribers: gets number of subs
    Args:
        subreddit: subreddit to query
    """
    subreddit = argv[1]
    base_url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"Use-Agent": "EMMA-SUB-COUNT"}
    try:
        res = requests.get(base_url, headers=headers, allow_redirects=False)
        data = res.json()
        sub = data['data']['subscribers']
        return sub
    except Exception as e:
        return 0
