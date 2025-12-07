# We will see the implemenation of sorting CSV data using Lambda functions 
# Refer to read_csv_sorted.py for detailed comments, this program is a modified version of that

# Lambda functions are small anonymous functions defined using the lambda keyword.
# They can take any number of arguments but can only have one expression.

footballers = [] # List to hold footballers' data

with open('names.csv') as csv_file:
    for line in csv_file:
        name, country = line.strip().split(',')
        footballer = {'name': name, 'country': country}
        footballers.append(footballer)

for footballer in sorted(footballers, key=lambda x: x['name']):
    print(f"Footballer's name is {footballer['name']} and the country is {footballer['country']}")        