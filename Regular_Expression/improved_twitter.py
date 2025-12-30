
import re

URL = input("Enter Twitter/X profile URL: ").strip()

# '?:' makes the group non-capturing
if username := re.search(r"^https?://(?:www\.)?x\.com/([a-zA-Z0-9_]+)$", URL, re.IGNORECASE):

    print(f"Name is",username.group(2))