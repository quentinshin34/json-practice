#!/usr/bin/env python3

import json # load json

# open json file and load data
with open('data/schacon.repos.json', 'r') as file:
    repos = json.load(file)

# open csv file called chacon.csv
with open('chacon.csv', 'w') as csv_file:
    for repo in repos[:5]: # first 5
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
        
        # formatting and write the line
        line = f"{name},{html_url},{updated_at},{visibility}\n"
        csv_file.write(line)
