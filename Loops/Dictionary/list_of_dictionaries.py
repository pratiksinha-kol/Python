

# Create a list of dictionary per footballer
footballers = [
    {"first_name": "Lionel", "last_name": "Messi", "club": "Barcelona"},
    {"first_name": "Cristiano", "last_name": "Ronaldo", "club": None},
    {"first_name": "Wayne", "last_name": "Rooney", "club": "Manchester United"},
    {"first_name": "Kylian", "last_name": "Mbappe", "club": "PSG"},
    {"first_name": "Robert", "last_name": "Lewandowski", "club": "Bayern Munich"}
]

for footballer in footballers:
    print(footballer["first_name"], footballer["last_name"], footballer["club"], sep=" ", end=", \n")


full_details = {
    "Pratik" : ["Sinha", "Miku"], 
    "Atindra" : ["Narayan", "Jagan"],
    "Rohit" : ["Sharma", "Shana"], 
    "Sourav" : ["Ganguly", "Dada"],
    "Virat" : ["Kohli", "Chiku"]
}

print(full_details["Sourav"][0]) # Accessing value using key and index
print(full_details["Pratik"][1]) # Accessing value using key and index
