#!/usr/bin/python3
""" A more advanced introduction to APIs in python
Access data from the Reddit API, process it, then generate an output.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts in a given subreddit. """

    # Check if given input is a string
    if not isinstance(subreddit, str):
        print(None)
        return

    # Declare variables used by function
    header = {'User-agent': "Donald's ALX_SE API"}
    query_str = {'t': 'all', 'limit': 10}
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

    # Fetch data from REST API
    request = requests.get(url, headers=header, params=query_str)

    # Locate and return number of subreddit subscribers, or 0 on error
    try:
        result = request.json()['data']['children']
        for post in result:
            print(post['data']['title'])
    except Exception:
        print(None)
        return


if __name__ == '__main__':
    """ Runs the program if not imported as a module. """

    if len(argv) >= 2:
        top_ten(argv[1])
    top_ten(['programming'])
    print(' - - - - - -')
    top_ten('programming')
    print(' - - - - - -')
    top_ten('this_is_a_fake_subreddit')
