import pprint

phonebook = {}

name = input("Name: ")
phone = input("Phone: ")
email = input("Email: ")
address = input("Address: ")

phonebook[phone] = {
    "name": name,
    "email": email,
    "address": address
}

pprint.pprint(phonebook)