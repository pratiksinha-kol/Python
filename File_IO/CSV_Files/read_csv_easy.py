# Reading a CSV file and printing formatted output
# This is a easier and more Pythonic way to read and unpack CSV data
# Refer to read_csv.py for a more detailed version (with comments)


# Note: We have used two variables to unpack the values directly from the split line
with open("names.csv") as file:
    for line in file:
        name, country = line.strip().split(",")
        print(f"Name of the footballer is {name} and the country is {country}")