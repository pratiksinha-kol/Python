

## A simple email validation script that checks for the presence of "@" in the email address.
## Entering '@' will be considered valid.

# your_email = input("Please enter your email address: ").strip()
# if "@" in your_email:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


## Another way to validate email addresses
## This version checks for both "@" and "." in the email address.
## Entering '@.' will be considered valid.

# my_email = input("Please enter your email address: ").strip()    
# if "@" in my_email and "." in my_email:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


## Another way to validate email addresses
## This version checks for the presence of "@" and ensures that there is a username before "@" and a domain with a "." after it.
## Entering '@.' will be considered invalid.

# test_email = input("Please enter your email address: ").strip()

# username, domain = test_email.split("@")

# if username and "." in domain:
#     print("Valid email address.")
# else:
#     print("Invalid email address.")


## Here's a more specific email validation script.
## This version checks for the presence of "@" and ensures that there is a username before "@" and that the domain ends with ".com".
## Entering 'a@.com' will be considered valid.

email = input("Please enter your email address: ").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("Valid email address.")
else:
    print("Invalid email address.")