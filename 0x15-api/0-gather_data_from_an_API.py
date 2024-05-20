#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            j_req = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            all_tsk = len(j_req)
            completed_tsk = []
            for t in j_req:
                if t.get("completed") is True:
                    completed_tsk.append(t)
            count = len(completed_tsk)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, all_tsk))
            for title in completed_tsk:
                print("\t {}".format(title.get("title")))
