import validators

text = input("What's your email address?")

if validators.email(text):
    print("Valid")
else:
    print("Invalid")