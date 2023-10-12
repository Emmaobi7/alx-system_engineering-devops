#!/usr/bin/python3
"""get employee TODO
    progress list
"""

import csv
import requests
from sys import argv


if __name__ == '__main__':
    url_name = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url_todo = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'

    res_user = requests.get(url_name)
    res_todo = requests.get(url_todo)
    user = res_user.json()
    todo = res_todo.json()
    username = user.get('username')

    with open(f'{argv[1]}.csv', 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerows(
                [argv[1], username, key.get('completed'), key.get('title')]
                for key in todo)
