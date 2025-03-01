import pprint


phonebook = {d
    "06 20 123 4567": {
        "name": "Kiss Csaba", 
        "adress": "Budapest", 
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

print(phonebook["06 20 123 4567"]["birth_date"])