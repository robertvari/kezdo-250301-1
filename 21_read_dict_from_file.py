import json, pprint

with open("phonebook.json") as file:
    phonebook = json.load(file)

pprint.pprint(phonebook)
print(phonebook["06 20 123 4567"]["name"])