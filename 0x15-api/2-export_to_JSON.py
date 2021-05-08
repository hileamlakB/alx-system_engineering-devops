#!/usr/bin/python3
"""
This gives an employee's todo
with some id, and exports it to
csv
"""
import json
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])

    todo_response = requests.get("{}todos?userId={}".format(base_url, emp_id))
    user_response = requests.get("{}users?id={}".format(base_url, emp_id))

    todo_lst = todo_response.json()
    name = user_response.json()[0].get("username")

    data = {str(emp_id): [{"task": todo.get("title"),
                          "completed": todo.get("completed"),
                           "username": name}
                          for todo in todo_lst]}

    with open("{}.json".format(emp_id), "w") as data_file:
        data_file.write(json.dumps(data))
