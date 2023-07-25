#!/usr/bin/python3
""" Introduction to APIs in python

Access data via API, organize it, then export it do different formats.
"""
import json
import requests
from sys import argv


def main():
    """ Uses a REST API to fetch employee info using a given employee ID,
    then exports all available tasks for the employee to a JSON file. """

    # Check if userID was given and exit if not
    if len(argv) == 1:
        exit(1)

    # Declare variables used by function
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    filename = '{}.json'.format(user_id)
    user, tasks_json = {}, []

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

    # Convert employee tasks to a list of dictionaries
    for item in tasks.json():
        task = {"task": item['title'],
                "completed": item['completed'],
                "username": user['username']
                }
        tasks_json.append(task)

    # Store JSON-formatted output in a JSON file
    with open(filename, "w", encoding="utf-8") as f:
        tasks_json = json.dumps({str(user['id']): tasks_json})
        f.write(tasks_json)
        # print(tasks_json)


if __name__ == '__main__':
    main()
