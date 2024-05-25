import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), 'wizyty.json')

clients = {
    "1": {
        "name": "Jan",
        "surname": "Kowalski",
        "email": "jan.kowalski@example.com",
        "phone": "123-456-789"
    },
    "2": {
        "name": "Anna",
        "surname": "Nowak",
        "email": "anna.nowak@example.com",
        "phone": "987-654-321"
    },
    "3": {
        "name": "Piotr",
        "surname": "Wiśniewski",
        "email": "piotr.wisniewski@example.com",
        "phone": "555-666-777"
    }
}

def przeliczanie_ceny (cena_netto):

    cena_brutto = cena_netto * 1.23
    return cena_brutto

def dodaj_wizyte():

    data = input("Data wizyty: (DD.MM.YYYY)")
    pacjent_id = input("ID pacjenta: ")
    choroba = input("Choroba: ")
    leki = input("Leki: ")
    cena_netto = float(input("Cena netto: "))
    cena_brutto = przeliczanie_ceny(cena_netto)

    wizyta = {"Data wizyty": data, 
            "Pacjent": clients.get(pacjent_id, None),
            "Choroba": choroba, 
            "Leki": leki, 
            "Cena": f"{cena_brutto}zł"}

    return wizyta

def zapisz_wizyte(wizyta): 

    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, 'r') as file:
                wizyty = json.load(file)
        except json.JSONDecodeError:
            print("Plik JSON jest pusty lub uszkodzony. Tworzenie nowego pliku.")
            wizyty = {}
    else:
        wizyty = {}

    wizyta_id = len(wizyty) + 1
    wizyty[wizyta_id] = wizyta

    with open(FILE_PATH, 'w') as file:
        json.dump(wizyty, file, indent=4)

wizyta = dodaj_wizyte()
zapisz_wizyte(wizyta)

new_wizyta = dodaj_wizyte()
zapisz_wizyte(new_wizyta)