import json, os

# create an empty phonebook dictionary
phonebook = {}

# IF phonebook exists
if os.path.exists("phonebook.json"):
    # open it and load it into phonebook dictionary
    with open("phonebook.json") as file:
        phonebook = json.load(file)

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