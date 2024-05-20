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
            alltsk = len(j_req)
            completedtsk = []
            for t in j_req:
                if t.get("completed") is True:
                    completedtsk.append(t)
            count = len(completedtsk)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, alltsk))
            for title in completedtsk:
                print("\t {}".format(title.get("title")))
