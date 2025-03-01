import pprint

phonebook = {
    "06 20 123 4567": {
        "name": "Kiss Csaba", 
        "address": "Budapest", 
        "email": "csaba@gmail.com",
        "birth_date": "1987-02-13"
        },

    "06 20 987 6543": {
        "name": "Kovács Tamás", 
        "address": "Pécs", 
        "email": "tamas@gmail.com",
        "birth_date": "1979-03-03"
        }
}

phonebook["06 20 123 4567"]["address"] = "Eger"
phonebook["06 30 123 4567"] = {"name": "Kovács Róbert", "email": "robert@gmail.com", "address": "Debrecen"}
pprint.pprint(phonebook)