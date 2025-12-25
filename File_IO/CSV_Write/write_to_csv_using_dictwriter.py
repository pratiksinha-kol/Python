# Write user-inputted book information to a CSV file
# The CSV file will contain the author's name, book title, and year of publication.
# We will use dict module to handle CSV file operations.
# Here we open the file in append mode to add new entries without overwriting existing data.

import csv

name = input("Enter author's name: ")
book = input("Enter book title: ")

with open('autobiographies.csv', mode='a', newline='') as file:
    # Create a DictWriter object
    # Specify the fieldnames for the CSV file
    # Write the data as a dictionary
    writer = csv.DictWriter(file, fieldnames=['author', 'title'])
    writer.writerow({'author': name, 'title': book})
print("Information added to autobiographies.csv")

file.close()
