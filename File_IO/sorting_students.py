# Using CSV module to read student data from a CSV file and sort by name

import csv

students = [] # List to hold students' data

with open('students.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        students.append({'name': row[0], 'address': row[1]})

for student in sorted(students, key=lambda x: x['name']):
    print(f"Name is {student['name']} resides in {student['address']}")    