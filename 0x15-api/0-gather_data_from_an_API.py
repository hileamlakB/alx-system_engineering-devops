#!/usr/bin/python3
"""
This gives an employees todo
with some id
"""
import sys
import requests


base_url = "https://jsonplaceholder.typicode.com/"
emp_id = int(sys.argv[1])

todo_response = requests.get("{}todos?userId={}".format(base_url, emp_id))
user_response = requests.get("{}users?userId={}".format(base_url, emp_id))

todo_lst = todo_response.json()
name = user_response.json()[0]["name"]

str_format = "Employee {} is done with tasks({}/{}):\n"
todo_str = ""
complete = 0
for todo in todo_lst:
    if todo["completed"]:
        complete += 1
    todo_str += "\t " + todo["title"] + "\n"

print(str_format.format(name, complete, len(todo_lst)) + todo_str[:-1])
