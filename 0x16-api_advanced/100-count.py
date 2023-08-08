#!/usr/bin/python3
""" A more advanced introduction to APIs in python
Access data from the Reddit API, process it, then generate an output.
"""
import requests
from sys import argv


def count_words(subreddit, word_list=[], __title_words=None,
                __hot_list='', __after='', __count=0):
    """ Parses the titles of all hot articles and pretty-prints a sorted
    count of given keywords.
    """
    # INPUT VALIDATION: Check if subreddit is string and two lists are lists
    if not isinstance(subreddit, str) or not isinstance(word_list, list):
        return

    if not __title_words:
        """ Recursively fetches and returns the titles of all the hot
        articles in a given subreddit.
        """
        # Declare variables used by request
        header = {'User-agent': "Donald's ALX_SE API"}
        query_str = {'t': 'all', 'limit': 100, 'after': __after,
                     'count': __count}
        url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)

        # Fetch data from REST API
        request = requests.get(url, headers=header, params=query_str)

        # Fetch titles of all hot articles and store all the words in a list
        try:
            prev_count = __count
            for post in request.json()['data']['children']:
                __hot_list += (post['data']['title'])
                __count += 1
                __after = post['data']['name']
            if __count > prev_count:
                count_words(subreddit, word_list, __title_words,
                            __hot_list, __after, __count)
                # This return ensures only last recursion passes this point
                return
            # Assignment in else ensures only last recursion passes this point
            else:
                __title_words = __hot_list
        except Exception:
            return

    if not __title_words:
        return
    word_counts = {}
    for word in word_list:
        word = str(word).lower()
        count = __title_words.lower().split().count(word)
        if count:
            if word in word_counts.keys():
                word_counts[word] += count
            else:
                word_counts[word] = count

    # Pretty-print results
    for key in sorted(word_counts.keys()):
        print('{}: {}'.format(key, word_counts[key]))


if __name__ == '__main__':
    """ Runs the program if not imported as a module. """

    if len(argv) >= 3:
        count_words(argv[1], argv[2].split())
    count_words('programming', ['developer'])
    count_words('programming',
                ['javA', 'JAVA', 'JavaScript', 8748934, 'ChatGPT', 'API'])
