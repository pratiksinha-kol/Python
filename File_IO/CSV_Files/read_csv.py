# This script reads a CSV file and prints each line as a list of values.
# You can remove 'r' as it is the default mode for opening a file
# FYI: The output will be sorted because we are using sorted() function

with open("names.csv") as file:
    for line in sorted(file):
        print(line.strip().split(","))
