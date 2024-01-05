import sys
from validator_collection import validators, errors

user_address = input("What's your email address? ")

try:
    email_address = validators.email(user_address)
except errors.EmptyValueError:
    print("Invalid")
    sys.exit(0)
except errors.InvalidEmailError:
    print("Invalid")
    sys.exit(0)

print("Valid")