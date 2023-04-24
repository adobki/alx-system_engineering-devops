#!/usr/bin/python3
""" Introduction to APIs in python

Access data via API, organize it, then export it do different formats.
"""
import json
import requests


def get_tasks(user_id):
    """ Uses a REST API to fetch employee info using a given employee
    ID, then returns all available tasks in a dictionary. """

    # Declare variables used by function
    url = 'https://jsonplaceholder.typicode.com/'
    user, tasks_dict = None, []

    # Fetch data from REST API
    employees = requests.get('{}users'.format(url))
    tasks = requests.get('{}todos?userId={}'.format(url, user_id))

    # Locate employee by given ID and set to user variable
    for item in employees.json():
        if item['id'] == int(user_id):
            user = item
            break
    if not user:
        return None

    # Convert employee tasks to a list of dictionaries and return it
    for item in tasks.json():
        task = {"username": user['username'],
                "task": item['title'],
                "completed": item['completed']
                }
        tasks_dict.append(task)

    return {str(user['id']): tasks_dict}


def main():
    """ Uses a REST API to fetch employee info for all available employee
    IDs, then exports all available tasks by employee ID to a JSON file. """

    # Declare variables used by function
    filename = 'todo_all_employees.json'
    all_tasks_dict, tasks_dict = {}, None

    # Fetch data from REST API
    employees = requests.get('https://jsonplaceholder.typicode.com/users')
    for user_id in range(1, len(employees.json()) + 2):
        tasks_dict = get_tasks(user_id)
        if tasks_dict:
            all_tasks_dict[str(user_id)] = tasks_dict[str(user_id)]

    # Store JSON-formatted output in a JSON file
    if len(all_tasks_dict):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json.dumps(all_tasks_dict))
            # print(json.dumps(all_tasks_dict))


if __name__ == '__main__':
    main()
