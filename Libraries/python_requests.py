# Install the requests package before running this code:
# pip install requests
# Request package is used to make HTTP/HTTPS requests in Python
# Import json package to handle JSON data

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()


# Using json.dumps() to pretty print JSON response
# and Indent parameter to define the number of spaces for indentation

# response = requests.get("https://api.github.com/users/" + sys.argv[1])
# print(response.json())
# print(json.dumps(response.json(), indent=2))

# Example API call to iTunes Search API
# requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=weezer")

# API call with user input 
response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
# print(response.json())

# Pretty print JSON response
print(json.dumps(response.json(), indent=2))

# Using 'output' variable to store JSON response and access specific data
# For example, printing track names from the response
# To extract specific information from the JSON response, we can execute the following:
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2))
# This will print the entire JSON response in a readable format (see above) 

output = response.json()
for result in output['results']:
    print("Track Name:", result['trackName'])
    print("Artist Name:", result['artistName'])
    print("Collection Name:", result['collectionName'])
    print()