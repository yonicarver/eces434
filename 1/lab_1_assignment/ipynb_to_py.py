#!/usr/bin/python3

import json

with open("Lab 1.ipynb", "r") as file:
    datastore = json.load(file)

for i in range(len(datastore['cells'])):
    if str(datastore['cells'][i]['cell_type']) == 'code':
        for item in datastore['cells'][i]['source']:
            print(item)
