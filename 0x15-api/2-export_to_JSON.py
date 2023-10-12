#!/usr/bin/python3
"""get employee TODO
    progress list
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url_name = f'https://jsonplaceholder.typicode.com/users/{argv[1]}'
    url_todo = f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}'

    res_user = requests.get(url_name)
    res_todo = requests.get(url_todo)
    user = res_user.json()
    todo = res_todo.json()
    username = user.get('username')
    data = {user_id: [{"task": i.get('title'), "completed":
            i.get('completed'), "username": username} for i in todo]}

    with open(f'{argv[1]}.json', 'w') as json_file:
        json.dump(data, json_file)
