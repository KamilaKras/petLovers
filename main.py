import json
import os
import clients
import visits
import data

FILE_PATH = os.path.join(os.path.dirname(__file__), 'wizyty.json')
LEKI_FILE_PATH = os.path.join(os.path.dirname(__file__), 'leki.json')

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

def przeliczanie_ceny(cena_netto):
    return cena_netto * 1.23

def dodaj_wizyte():
    data = input("Data wizyty: (DD.MM.YYYY) ")
    pacjent_id = input("ID pacjenta: ")
    choroba = input("Choroba: ")
    leki = input("Leki: ")
    cena_netto = float(input("Cena netto: "))
    cena_brutto = przeliczanie_ceny(cena_netto)

    wizyta = {
        "Data wizyty": data,
        "Pacjent": clients.get(pacjent_id, None),
        "Choroba": choroba,
        "Leki": leki,
        "Cena": f"{cena_brutto}zł"
    }
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

def wczytaj_dane(plik):
    if not os.path.exists(plik):
        return []
    with open(plik, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def zapisz_dane(plik, dane):
    with open(plik, 'w') as file:
        json.dump(dane, file, indent=4)

def generuj_id_zwierzecia(klienci):
    if not klienci:
        return '001'
    ids = [int(k['id_zwierzecia']) for k in klienci]
    return str(max(ids) + 1).zfill(3)

def znajdz_klienta_po_id(klienci, id_zwierzecia):
    for klient in klienci:
        if klient['id_zwierzecia'] == id_zwierzecia:
            return klient
    return None

def dodaj_klienta(klienci, plik):
    id_zwierzecia = generuj_id_zwierzecia(klienci)
    imie = input("Podaj imię właściciela: ")
    nazwisko = input("Podaj nazwisko właściciela: ")
    email = input("Podaj email właściciela: ")
    telefon = input("Podaj telefon właściciela: ")
    imie_zwierzecia = input("Podaj imię zwierzęcia: ")
    wiek_zwierzecia = input("Podaj wiek zwierzęcia: ")
    rasa = input("Podaj rasę zwierzęcia: ")

    klient = {
        "id_zwierzecia": id_zwierzecia,
        "imie": imie,
        "nazwisko": nazwisko,
        "email": email,
        "telefon": telefon,
        "zwierze": {
            "imie_zwierzecia": imie_zwierzecia,
            "wiek_zwierzecia": wiek_zwierzecia,
            "rasa": rasa
        }
    }
    klienci.append(klient)
    zapisz_dane(plik, klienci)
    print(f"Klient {imie} {nazwisko} został dodany do bazy danych z ID {id_zwierzecia}.")

def aktualizuj_klienta(klienci, plik):
    id_zwierzecia = input("Podaj ID zwierzęcia do aktualizacji: ")
    klient = znajdz_klienta_po_id(klienci, id_zwierzecia)
    if klient:
        klient['imie'] = input(f"Podaj nowe imię właściciela ({klient['imie']}): ") or klient['imie']
        klient['nazwisko'] = input(f"Podaj nowe nazwisko właściciela ({klient['nazwisko']}): ") or klient['nazwisko']
        klient['email'] = input(f"Podaj nowy email właściciela ({klient['email']}): ") or klient['email']
        klient['telefon'] = input(f"Podaj nowy telefon właściciela ({klient['telefon']}): ") or klient['telefon']
        klient['zwierze']['imie_zwierzecia'] = input(f"Podaj nowe imię zwierzęcia ({klient['zwierze']['imie_zwierzecia']}): ") or klient['zwierze']['imie_zwierzecia']
        klient['zwierze']['wiek_zwierzecia'] = input(f"Podaj nowy wiek zwierzęcia ({klient['zwierze']['wiek_zwierzecia']}): ") or klient['zwierze']['wiek_zwierzecia']
        klient['zwierze']['rasa'] = input(f"Podaj nową rasę zwierzęcia ({klient['zwierze']['rasa']}): ") or klient['zwierze']['rasa']
        
        zapisz_dane(plik, klienci)
        print(f"Dane klienta o ID {id_zwierzecia} zostały zaktualizowane.")
    else:
        print(f"Klient o ID {id_zwierzecia} nie został znaleziony.")

def wyswietl_liste_klientow(klienci):
    if not klienci:
        print("Brak klientów w bazie danych.")
    else:
        for klient in klienci:
            zwierze = klient['zwierze']
            print(f"ID: {klient['id_zwierzecia']}, Imię: {klient['imie']}, Nazwisko: {klient['nazwisko']}, "
                  f"Email: {klient['email']}, Telefon: {klient['telefon']}, "
                  f"Zwierzę: {zwierze['imie_zwierzecia']}, Wiek: {zwierze['wiek_zwierzecia']}, Rasa: {zwierze['rasa']}")

def wczytaj_leki():
    if not os.path.exists(LEKI_FILE_PATH):
        return {}
    with open(LEKI_FILE_PATH, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def zapisz_leki(leki):
    with open(LEKI_FILE_PATH, 'w') as file:
        json.dump(leki, file, indent=4)

def dodaj_lek():
    leki = wczytaj_leki()
    nazwa = input("Podaj nazwę leku: ")
    ilosc = int(input("Podaj ilość: "))
    dostawca = input("Podaj dostawcę: ")

    if nazwa in leki:
        print("Lek już istnieje w bazie.")
    else:
        leki[nazwa] = {
            "ilosc": ilosc,
            "dostawca": dostawca
        }
        zapisz_leki(leki)
        print(f"Lek {nazwa} został dodany do bazy danych.")

def usun_lek():
    leki = wczytaj_leki()
    nazwa = input("Podaj nazwę leku do usunięcia: ")

    if nazwa in leki:
        del leki[nazwa]
        zapisz_leki(leki)
        print(f"Lek {nazwa} został usunięty z bazy danych.")
    else:
        print("Lek nie istnieje w bazie.")

def edytuj_lek():
    leki = wczytaj_leki()
    nazwa = input("Podaj nazwę leku do edytowania: ")

    if nazwa in leki:
        nowa_ilosc = int(input(f"Podaj nową ilość dla {nazwa}: "))
        leki[nazwa]["ilosc"] = nowa_ilosc
        zapisz_leki(leki)
        print(f"Ilość leku {nazwa} została zaktualizowana.")
    else:
        print("Lek nie istnieje w bazie.")

def main():
    plik = 'clients.json'
    klienci = data.wczytaj_dane(plik)
    plik_wizyt = 'wizyty.json'
    klienci_plik = 'clients.json'
    klienci = wczytaj_dane(klienci_plik)

    while True:
        print("\n1. Dodaj/Zaktualizuj dane klienta")
        print("2. Wyświetl listę klientów")
        print("3. Dodaj wizytę")
        print("4. Wyświetl wszystkie wizyty")
        print("5. Wyświetl wizyty konkretnego pacjenta")
        print("6. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3/4/5/6): ")
        print("3. Dodaj wizytę")
        print("4. Dodaj lek")
        print("5. Usuń lek")
        print("6. Edytuj lek")
        print("7. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3/4/5/6/7): ")

        if wybor == '1':
            pod_wybor = input("Czy chcesz dodać nowego klienta (D) czy zaktualizować dane istniejącego klienta (A)? (D/A): ").upper()
            if pod_wybor == 'D':
                clients.dodaj_klienta(klienci, plik)
                dodaj_klienta(klienci, klienci_plik)
            elif pod_wybor == 'A':
                clients.aktualizuj_klienta(klienci, plik)
                aktualizuj_klienta(klienci, klienci_plik)
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor == '2':
            clients.wyswietl_liste_klientow(klienci)
        elif wybor == '3':
            wizyta = visits.dodaj_wizyte(klienci)
            if wizyta:
                visits.zapisz_wizyte(wizyta, plik_wizyt)
                print("Dodano nową wizytę")
        elif wybor == '4':
            visits.wyswietl_wszystkie_wizyty(plik_wizyt)
        elif wybor == '5':
            id_pacjenta = input("Podaj ID pacjenta: ")
            visits.wyswietl_wizyty_pacjenta(plik_wizyt, id_pacjenta)
        elif wybor == '6':
            wizyta = dodaj_wizyte()
            zapisz_wizyte(wizyta)
        elif wybor == '4':
            dodaj_lek()
        elif wybor == '5':
            usun_lek()
        elif wybor == '6':
            edytuj_lek()
        elif wybor == '7':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
 
