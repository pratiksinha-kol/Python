# Reading a CSV file, sorting the lines, and printing formatted output

# Approach 1: Sorting lines directly while reading
footballers = []

# with open("names.csv") as file:
#     for line in sorted(file):
#         name, country = line.strip().split(",")
#         print(f"Name of the footballer is {name} and the country is {country}")

# We are sorting based on the entire line and not just the name or country.

# Approach 2: Collecting data first, then sorting and printing 
# We have used a list to collect footballers' data (refer to line 4)

# with open("names.csv") as file:
#     for line in file:
#         name, country = line.strip().split(",")
#         # Collecting footballers' data into a list
#         footballers.append(f" This footballer's name is {name} and the country is {country}")

# for footballer in sorted(footballers):
#     print(footballer)            


# Approach 3: Sorting by name using a list of dictionaries
# Created a dictonary for each footballer to hold name and country (refer to line 33)
# We will now sort it by name only

with open("names.csv") as file:
    for line in file:
        name, country = line.strip().split(",")

        # Creating a dictionary to hold name and country
        # footballer = {}
        # footballer['name'] = name
        # footballer['country'] = country
        
        # Easier way to create dictionary
        footballer = {'name': name, 'country': country}
        
        
        # Collecting footballers' data into a list of dictionaries to sort by name (see dictionary created in line 33)
        footballers.append(footballer) # Adding dictionary to the list of 'footballers'

# We can define a function to get the name from dictionary for sorting
def get_name(footballer):
    return footballer['name']

def get_country(footballer):
    return footballer['country']

for name_footballer in sorted(footballers, key=get_name, reverse=True):
    print(f"Footballer's name is {name_footballer['name']} and the country is {name_footballer['country']}\n")        

for name_footballer in sorted(footballers, key=get_country):
    print(f"Name is {name_footballer['name']} and the country is {name_footballer['country']}")            
