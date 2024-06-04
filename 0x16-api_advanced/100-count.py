#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
"""
import requests
from collections import Counter


def count_words(subreddit, word_list, hot_list=[], after=None, counts=None):
    '''Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        found_list (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    '''
    if counts is None:
        counts = Counter()

    # Convert word_list to lowercase for case-insensitive matching
    word_list = [word.lower() for word in word_list]

    # Base URL for the subreddit's hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Add the titles of the posts to the hot_list
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        # Get the 'after' value for the next page of results
        after = data['data']['after']

        if after is not None:
            # Recursive call to get the next page of results
            return count_words(subreddit, word_list, hot_list, after, counts)
        else:
            # Process all titles to count keyword occurrences
            for title in hot_list:
                words = title.lower().split()
                for word in word_list:
                    counts[word] += words.count(word)

            # Filter and sort results
            sorted_counts = sorted(counts.items(),
                                   key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")

            return
    else:
        return
