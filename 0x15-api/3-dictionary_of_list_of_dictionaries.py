#!/usr/bin/python3
"""
This gives an employee's todo
with some id, and exports it to
csv
"""
import json
import requests
import sys


base_url = "https://jsonplaceholder.typicode.com/"

user_response = requests.get("{}users".format(base_url))


data = {}
for user in user_response.json():

    todo_response = requests.get(
        "{}todos?userId={}".format(base_url, user["id"]))
    todos = todo_response.json()

    data[user["id"]] = [{"task": todo["title"], "completed":todo["completed"], "username":user["name"]}
                        for todo in todos]

with open("todo_all_employees.json", "w") as data_file:
    data_file.write(json.dumps(data))
