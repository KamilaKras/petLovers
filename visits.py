import datetime
import json
import os
import clients

def waliduj_date(date_text):
    try:
        data_wizyty = datetime.datetime.strptime(date_text, '%d.%m.%Y')
        return data_wizyty
    except ValueError:
        return None

def przeliczanie_ceny (cena_netto):
    if isinstance(cena_netto, str) and cena_netto == "Brak danych":
        return "Brak danych"
    cena_brutto = cena_netto * 1.08
    cena_brutto = f"{cena_brutto:.2f}"
    cena_brutto = cena_brutto.replace('.', ',')
    cena_brutto = f"{cena_brutto} zł"
    return cena_brutto

def dodaj_wizyte(klienci, pacjent_id):
    data_wizyty = input("Data wizyty (DD.MM.RRRR): ").strip()
    data_wizyty_obj = waliduj_date(data_wizyty)
    while not data_wizyty_obj:
        print("Nieprawidłowy format daty. Spróbuj ponownie.")
        data_wizyty = input("Data wizyty (DD.MM.RRRR): ").strip()
        data_wizyty_obj = waliduj_date(data_wizyty)

    if data_wizyty_obj.date() > datetime.date.today():
        potwierdzenie = input("Podana data jest w przyszłości. Czy na pewno chcesz kontynuować? (tak/nie): ").strip().lower()
        if potwierdzenie != 'tak':
            print("Anulowano dodawanie wizyty.")
            return

    pacjent = clients.znajdz_klienta_po_id(klienci, pacjent_id)
    if not pacjent:
        print("Nie znaleziono pacjenta o podanym ID. Anulowano dodawanie wizyty.")
        return

    choroba = input("Choroba: ").strip() or "Brak danych"
    leki = input("Leki: ").strip() or "Brak danych"
    dawkowanie = input("Dawkowanie: ").strip() or "Brak danych"
    notatki = input("Dodatkowe informacje: ").strip() or "Brak danych"

    cena_netto_input = input("Cena netto: ").strip().replace(',', '.')
    try:
        cena_netto = float(cena_netto_input) if cena_netto_input else "Brak danych"
    except ValueError:
        cena_netto = "Brak danych"

    cena_brutto = przeliczanie_ceny(cena_netto)

    wizyta = {
        "Data wizyty": data_wizyty,
        "Pacjent": pacjent_id,
        "Choroba": choroba,
        "Recepta": {
            "Leki": leki,
            "Dawkowanie": dawkowanie
        },
        "Dodatkowe informacje": notatki,
        "Cena netto": cena_netto,
        "Cena brutto": cena_brutto
    }

    return wizyta

def zapisz_wizyte(wizyta, plik_wizyt):
    try:
        if os.path.exists(plik_wizyt):
            with open(plik_wizyt, 'r', encoding='utf-8') as file:
                wizyty = json.load(file)
        else:
            wizyty = {}
    except json.JSONDecodeError:
        print("Plik JSON jest pusty lub uszkodzony. Tworzenie nowego pliku.")
        wizyty = {}

    wizyta_id = len(wizyty) + 1
    wizyty[wizyta_id] = wizyta

    with open(plik_wizyt, 'w', encoding='utf-8') as file:
        json.dump(wizyty, file, indent=4, ensure_ascii=False)

    print(f"Dodano wizytę. Cena brutto wizyty wynosi: {wizyta['Cena brutto']}")

def wyswietl_wszystkie_wizyty(plik_wizyt):
    if not os.path.exists(plik_wizyt):
        print("Brak zapisanych wizyt.")
        return

    try:
        with open(plik_wizyt, 'r', encoding='utf-8') as file:
            wizyty = json.load(file)
        if not wizyty:
            print("Brak zapisanych wizyt.")
        else:
            print("Wszystkie zarejestrowane wizyty:")
            for id_wizyty, wizyta in wizyty.items():
                recepta = wizyta['Recepta']
                print(f"Wizyta ID: {id_wizyty}, Data: {zamien_none_na_brak_danych(wizyta['Data wizyty'])}, Pacjent ID: {zamien_none_na_brak_danych(wizyta['Pacjent'])}, Choroba: {zamien_none_na_brak_danych(wizyta['Choroba'])}, "
                      f"Leki: {zamien_none_na_brak_danych(recepta['Leki'])}, Dawkowanie: {zamien_none_na_brak_danych(recepta['Dawkowanie'])}, "
                      f"Dodatkowe informacje: {zamien_none_na_brak_danych(wizyta['Dodatkowe informacje'])}, Cena netto: {formatuj_cene(wizyta['Cena netto'])}, Cena brutto: {wizyta['Cena brutto']}")
    except json.JSONDecodeError:
        print("Błąd podczas wczytywania danych wizyt.")

def wyswietl_wizyty_pacjenta(plik_wizyt, id_pacjenta):
    if not os.path.exists(plik_wizyt):
        print("Brak zapisanych wizyt.")
        return

    try:
        with open(plik_wizyt, 'r', encoding='utf-8') as file:
            wizyty = json.load(file)
        if not wizyty:
            print("Brak zapisanych wizyt.")
        else:
            print(f"Wizyty dla pacjenta o ID {id_pacjenta}:")
            for id_wizyty, wizyta in wizyty.items():
                if wizyta['Pacjent'] == id_pacjenta:
                    recepta = wizyta['Recepta']
                    print(f"Wizyta ID: {id_wizyty}, Data: {zamien_none_na_brak_danych(wizyta['Data wizyty'])}, Choroba: {zamien_none_na_brak_danych(wizyta['Choroba'])}, "
                          f"Leki: {zamien_none_na_brak_danych(recepta['Leki'])}, Dawkowanie: {zamien_none_na_brak_danych(recepta['Dawkowanie'])}, "
                          f"Dodatkowe informacje: {zamien_none_na_brak_danych(wizyta['Dodatkowe informacje'])}, Cena netto: {formatuj_cene(wizyta['Cena netto'])}, Cena brutto: {wizyta['Cena brutto']}")
    except json.JSONDecodeError:
        print("Błąd podczas wczytywania danych wizyt.")

def zamien_none_na_brak_danych(wartosc):
    if wartosc is None or wartosc == "None":
        return "Brak danych"
    return wartosc

def formatuj_cene(cena):
    if cena == "Brak danych":
        return cena
    cena = f"{cena:.2f}".replace('.', ',')
    return f"{cena} zł"
