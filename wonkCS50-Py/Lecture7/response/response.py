import validators

v = validators.email(input("Input: "))
if v: print("Valid")
else: print("Invalid")
