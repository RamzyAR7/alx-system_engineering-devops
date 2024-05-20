#!/usr/bin/python3
'''
Using what you did in the task #0
extend your Python script to export data in the JSON format.
'''
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"
    us = requests.get(url, verify=False).json()
    doc = {}
    udoc = {}
    for user in us:
        uid = user.get("id")
        udoc[uid] = []
        doc[uid] = user.get("username")
    url = "https://jsonplaceholder.typicode.com/todos"
    todo = requests.get(url, verify=False).json()
    [udoc.get(t.get("userId")).append({"task": t.get("title"),
                                       "completed": t.get("completed"),
                                       "username": doc.get(
                                               t.get("userId"))})
     for t in todo]
    with open("todo_all_employees.json", 'w') as file:
        json.dump(udoc, file)
