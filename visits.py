import json
import os
import clients

def przeliczanie_ceny (cena_netto):

    cena_brutto = cena_netto * 1.23
    return round(cena_brutto, 2)

def dodaj_wizyte(klienci):

    data = input("Data wizyty: (DD.MM.YYYY): ")
    pacjent_id = input("ID pacjenta: ")
    choroba = input("Choroba: ")
    leki = input("Leki: ")
    cena_netto = float(input("Cena netto: "))
    cena_brutto = przeliczanie_ceny(cena_netto)

    pacjent = clients.znajdz_klienta_po_id(klienci, pacjent_id)
    if not pacjent:
        print("Nie znaleziono pacjenta.")
        return None

    wizyta = {
            "Data wizyty": data, 
            "Pacjent": pacjent_id,
            "Choroba": choroba, 
            "Leki": leki, 
            "Cena netto": cena_netto,
            "Cena brutto": cena_brutto
            }

    return wizyta

def zapisz_wizyte(wizyta, plik_wizyt): 
    try:
        if os.path.exists(plik_wizyt):
            with open(plik_wizyt, 'r') as file:
                wizyty = json.load(file)
        else:
            wizyty = {}
    
    except json.JSONDecodeError:
            print("Plik JSON jest pusty lub uszkodzony. Tworzenie nowego pliku.")
            wizyty = {}
    
    wizyta_id = len(wizyty) + 1
    wizyty[wizyta_id] = wizyta

    with open(plik_wizyt, 'w') as file:
        json.dump(wizyty, file, indent=4)
    
    print(f"Dodano wizytę. Cena brutto wizyty wynosi: {wizyta['Cena brutto']} zł")


def wyswietl_wszystkie_wizyty(plik_wizyt):
    if not os.path.exists(plik_wizyt):
        print("Brak zapisanych wizyt.")
        return

    try:
        with open(plik_wizyt, 'r') as file:
            wizyty = json.load(file)
        if not wizyty:
            print("Brak zapisanych wizyt.")
        else:
            print("Wszystkie zarejestrowane wizyty:")
            for id_wizyty, wizyta in wizyty.items():
                print(f"Wizyta ID: {id_wizyty}, Data: {wizyta['Data wizyty']}, Pacjent ID: {wizyta['Pacjent']}, Choroba: {wizyta['Choroba']}, Leki: {wizyta['Leki']}, Cena brutto: {wizyta['Cena brutto']}")
    except json.JSONDecodeError:
        print("Błąd podczas wczytywania danych wizyt.")

def wyswietl_wizyty_pacjenta(plik_wizyt, id_pacjenta):
    if not os.path.exists(plik_wizyt):
        print("Brak zapisanych wizyt.")
        return

    try:
        with open(plik_wizyt, 'r') as file:
            wizyty = json.load(file)
        if not wizyty:
            print("Brak zapisanych wizyt.")
        else:
            print(f"Wizyty dla pacjenta o ID {id_pacjenta}:")
            znaleziono_wizyty = False
            for id_wizyty, wizyta in wizyty.items():
                if wizyta['Pacjent'] == id_pacjenta:
                    znaleziono_wizyty = True
                    print(f"Wizyta ID: {id_wizyty}, Data: {wizyta['Data wizyty']}, Choroba: {wizyta['Choroba']}, Leki: {wizyta['Leki']}, Cena brutto: {wizyta['Cena brutto']}")
            if not znaleziono_wizyty:
                print("Nie znaleziono wizyt dla tego pacjenta.")
    except json.JSONDecodeError:
        print("Błąd podczas wczytywania danych wizyt.")
