# Request four inputs for each piece of data, assigning these to variable
name = input("What is your Name? ")
age = input("What is your Age? ")
house_number = input("What is your House Number? ")
street_name = input("What is your Street Name? ")

# Build a print statment using an f string to return the user variables
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name} Street.")