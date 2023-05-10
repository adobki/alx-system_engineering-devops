#!/usr/bin/python3
""" A more advanced introduction to APIs in python

Access data from the Reddit API, process it, then generate an output.
"""
import requests
from sys import argv


def recurse(subreddit, hot_list=[], __after='', __count=0):
    """ Recursively fetches and returns the titles
    of all the hot articles in a given subreddit.
    """
    # INPUT VALIDATION: Check if subreddit is string and __hot_list is list
    if not isinstance(subreddit, str):
        return
    if not isinstance(hot_list, list):
        hot_list = []

    # Declare variables used by function
    header = {'User-agent': "Donald's ALX_SE API"}
    query_str = {'t': 'all', 'limit': 100, 'after': __after, 'count': __count}
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    # Fetch data from REST API
    request = requests.get(url, headers=header, params=query_str)

    # Locate and return number of subreddit subscribers, or 0 on error
    try:
        result = []
        prev_count = __count
        for post in request.json()['data']['children']:
            hot_list.append(post['data']['title'])
            __count += 1
            __after = post['data']['name']
        if __count > prev_count:
            result = recurse(subreddit, hot_list, __after, __count)
            if result:
                return result
        return hot_list
    except Exception:
        return


if __name__ == '__main__':
    """ Runs the program if not imported as a module. """

    if len(argv) >= 2:
        print(recurse(argv[1]))
    print(' - - - - - -')
    print(recurse(['programming']))
    print(' - - - - - -')
    print(recurse('programming', 'a string', 8748934, 900))
    print(' - - - - - -')
    output = recurse('programming')
    print(f'Number of hot articles: {len(output)}')
    print(output)
    print(' - - - - - -')
    print(recurse('this_is_a_fake_subreddit'))
