#!/usr/bin/python3
""" A more advanced introduction to APIs in python
Access data from the Reddit API, process it, then generate an output.
"""
import requests
from sys import argv


def number_of_subscribers(subreddit):
    """ Returns number of total subscribers for a given subreddit. """

    # Check if given input is a string
    if not isinstance(subreddit, str):
        return 0

    # Declare variables used by function
    header = {'User-agent': "Donald's ALX_SE API"}
    url = 'https://reddit.com/r/{}/top.json'.format(subreddit)

    # Fetch data from REST API
    request = requests.get(url, headers=header)

    # Locate and return number of subreddit subscribers, or 0 on error
    try:
        result = request.json()['data']['children'][0]['data']
        return result['subreddit_subscribers']
    except Exception:
        return 0


if __name__ == '__main__':
    """ Runs the program if not imported as a module. """

    if len(argv) >= 2:
        print(number_of_subscribers(argv[1]))
    print(number_of_subscribers(['programming']))
    print(number_of_subscribers('programming'))
    print(number_of_subscribers('this_is_a_fake_subreddit'))
