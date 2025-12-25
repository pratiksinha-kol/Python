# Write user-inputted book information to a CSV file
# The CSV file will contain the author's name, book title, and year of publication.
# We will use the csv module to handle CSV file operations.
# Here we open the file in append mode to add new entries without overwriting existing data.

import csv

name = input("Enter author's name: ")
book = input("Enter book title: ")
year = input("Enter year of publication: ")

with open('books.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([name, book, year])
print("Book information added to books.csv")
