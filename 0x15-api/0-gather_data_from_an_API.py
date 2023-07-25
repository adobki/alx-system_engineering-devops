#!/usr/bin/python3
""" Introduction to APIs in python

Access data via API, organize it, then export it do different formats.
"""
import requests
from sys import argv


def main():
    """ Uses a REST API to fetch employee info using a given employee ID. """

    # Check if userID was given and exit if not
    if len(argv) == 1:
        exit(1)

    # Declare variables used by function
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user, completed = {}, []

    # Fetch data from REST API
    employees = requests.get('{}users'.format(url))
    tasks = requests.get('{}todos?userId={}'.format(url, user_id))

    # Locate employee by given ID and set to user variable
    for item in employees.json():
        if item['id'] == int(user_id):
            user = item
            break
    if not user:
        print('Sorry, employee with userID={} not found!'.format(user_id))
        exit(1)

    # Locate completed tasks for given employee
    for item in tasks.json():
        if item['completed']:
            completed.append(item['title'])

    # Pretty-print formatted output
    print('Employee {} is done with tasks({}/{}):'
          .format(user['name'], len(completed), len(tasks.json())))
    [print('\t {}'.format(item)) for item in completed]


if __name__ == '__main__':
    main()
