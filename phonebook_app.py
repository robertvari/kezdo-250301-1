import json, os

phonebook = {}

# clear terminal
os.system("cls")
print("-"*50, "Phonebook App", "-"*50)

# Get data from terminal with input()
phone = input("Phone: ")
name = input("Name: ")
email = input("Email: ")
address = input("Address: ")

# Build dictionary with data
phonebook[phone] = {
    "name": name,
    "email": email,
    "address": address
}

# Save data to file
with open("phonebook.json", "w") as file:
    json.dump(phonebook, file)

print("Your data was saved :)))")
print("-"*120)