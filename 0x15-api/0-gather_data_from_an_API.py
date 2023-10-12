#!/usr/bin/python3
"""get employee TODO
    progress list
"""

import requests
from sys import argv


if __name__ == '__main__':
    url_name = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url_todo = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'

    response_user = requests.get(url_name)
    response_todo = requests.get(url_todo)
    user = response_user.json()
    todo = response_todo.json()
    employee_name = user.get('name')
    num_tasks = len(todo)
    done = 0
    for key in todo:
        if key.get('completed'):
            c = key.get('title')
            done += 1
    print(f'Employee {employee_name} is done with tasks({done}/{num_tasks})')
    for key in todo:
        if key.get('completed'):
            print('\t {}'.format(key.get('title')))
