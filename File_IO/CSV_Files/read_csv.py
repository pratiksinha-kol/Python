# This script reads a CSV file and prints each line as a list of values.
# You can remove 'r' as it is the default mode for opening a file
# FYI: The output will be sorted because we are using sorted() function

with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")  # Remove trailing whitespace and split by comma
        print(f"Footballer's name is {row[0]} and the country is{ row[1]}")

# We have used for loop to read each line of the file
# rstrip() method is used to remove any trailing whitespace characters including newline
# split(",") method is used to split the line into a list of values based on comma
# Finally, we print the values in a formatted string
# Note: We have used indexing to access specific elements in the list        