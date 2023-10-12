#!/usr/bin/python3
"""get employee TODO
    progress list
"""

import csv
import json
import requests
from sys import argv


if __name__ == '__main__':
    url_name = f'https://jsonplaceholder.typicode.com/users'

    res_user = requests.get(url_name)
    users = res_user.json()
    data = {user.get('id'): [{"username": user.get('username'), "task":
            i.get('title'), "completed": i.get('completed')}
        for i in requests.get('https://jsonplaceholder.typicode.com/todos',
                              params={"userId": user.get('id')}).json()]
            for user in users}

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
