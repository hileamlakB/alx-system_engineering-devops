#!/usr/bin/python3
"""
This gives an employee's todo
with some id, and exports it to
csv
"""
import csv
import requests
import sys


if __name__ == '__main__':
    base_url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(sys.argv[1])

    todo_response = requests.get("{}todos?userId={}".format(base_url, emp_id))
    user_response = requests.get("{}users?userId={}".format(base_url, emp_id))

    todo_lst = todo_response.json()
    name = user_response.json()[0].get("name")

    with open("{}.csv".format(emp_id), "w") as data_file:
        csv_writer = csv.writer(data_file,
                                quotechar='\"',
                                quoting=csv.QUOTE_ALL)
        for todo in todo_lst:
            csv_writer.writerow(
                [str(emp_id),
                 name,
                 str(todo.get("completed")),
                 todo.get("title")])
