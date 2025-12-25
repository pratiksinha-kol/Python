# sorting_cricketers.py
# This script reads a CSV file containing cricketers' names and their countries
# We use csv.DictReader to read the file and store the data in a list of dictionaries
# Finally, we sort the list by cricketer names and print them

import csv

cricketers = []

with open('cricketers_name.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cricketers.append({"name": row["Name"], "country": row["Country"]})

for cricketer in sorted(cricketers, key=lambda cricketer: cricketer["name"]):
    print(f"{cricketer['name']} is from {cricketer['country']}")        