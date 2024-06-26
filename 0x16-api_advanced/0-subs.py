#!/usr/bin/python3
"""
function that queries the Reddit API.
"""

import requests


def number_of_subscribers(subreddit):
    """URL for the subreddit's about.json endpoint"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
