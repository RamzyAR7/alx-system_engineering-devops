#!/usr/bin/python3
'''
Using what you did in the task #0
extend your Python script to export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    t = [{"task": t.get("title"),
          "username": name,
          "completed": t.get("completed")} for t in todo]
    js_t = {}
    js_t[uid] = t
    with open("{}.json".format(uid), 'w') as file:
        json.dump(js_t, file)
