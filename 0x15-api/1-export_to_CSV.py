#!/usr/bin/python3
""" Introduction to APIs in python

Access data via API, organize it, then export it do different formats.
"""
import requests
from sys import argv


def main():
    """ Uses a REST API to fetch employee info using a given employee ID,
    then exports all available tasks for the employee to a CSV file. """

    # Check if userID was given and exit if not
    if len(argv) == 1:
        exit(1)

    # Declare variables used by function
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    filename = '{}.csv'.format(user_id)
    user = {}

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

    # Convert employee tasks to given csv format and store in csv file
    with open(filename, "w", encoding="utf-8") as f:
        for item in tasks.json():
            task = '"{}","{}","{}","{}"\n'.format(
                                  user['id'], user['username'],
                                  item['completed'], item['title']
                                 )
            f.write(task)
            # print(task, end='')


if __name__ == '__main__':
    main()
