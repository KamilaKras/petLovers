import json
import os

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
    wiek_zwierzecia = input("Podaj wiek zwierzęcia w latach: ")
    typ_zwierzecia = input("Podaj typ zwierzęcia (np. kot, pies): ")
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
            "typ_zwierzecia": typ_zwierzecia,
            "rasa": rasa
        }
    }
    klienci.append(klient)
    zapisz_dane(plik, klienci)
    print(f"Klient {imie} {nazwisko} został dodany do bazy danych z ID {id_zwierzecia}.")

def aktualizuj_klienta(klienci, plik):
    id_zwierzecia = input("Przechodzisz do edycji informacji o zwierzęciu. Jeżeli nie chcesz zmieniać informacji, o którą zostaniesz zapytany, pomiń ją. Podaj ID zwierzęcia do aktualizacji: ")
    klient = znajdz_klienta_po_id(klienci, id_zwierzecia)
    if klient:
        klient['imie'] = input(f"Podaj nowe imię właściciela ({klient['imie']}): ") or klient['imie']
        klient['nazwisko'] = input(f"Podaj nowe nazwisko właściciela ({klient['nazwisko']}): ") or klient['nazwisko']
        klient['email'] = input(f"Podaj nowy email właściciela ({klient['email']}): ") or klient['email']
        klient['telefon'] = input(f"Podaj nowy telefon właściciela ({klient['telefon']}): ") or klient['telefon']
        klient['zwierze']['imie_zwierzecia'] = input(f"Podaj nowe imię zwierzęcia ({klient['zwierze']['imie_zwierzecia']}): ") or klient['zwierze']['imie_zwierzecia']
        klient['zwierze']['wiek_zwierzecia'] = input(f"Podaj nowy wiek zwierzęcia ({klient['zwierze']['wiek_zwierzecia']}): ") or klient['zwierze']['wiek_zwierzecia']
        klient['zwierze']['typ_zwierzecia'] = input(f"Podaj nowy typ zwierzęcia ({klient['zwierze']['typ_zwierzecia']}): ") or klient['zwierze']['typ_zwierzecia']
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
            
def przeliczanie_ceny (cena_netto):

    cena_brutto = cena_netto * 1.23
    return cena_brutto

def dodaj_wizyte(klienci):

    data = input("Data wizyty: (DD.MM.YYYY): ")
    pacjent_id = input("ID pacjenta: ")
    choroba = input("Choroba: ")
    leki = input("Leki: ")
    cena_netto = float(input("Cena netto: "))
    cena_brutto = przeliczanie_ceny(cena_netto)

    pacjent = znajdz_klienta_po_id(klienci, pacjent_id)
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


def main():
    plik = 'clients.json'
    klienci = wczytaj_dane(plik)
    plik_wizyt = 'wizyty.json'

    while True:
        print("\n1. Dodaj/Zaktualizuj dane klienta")
        print("2. Wyświetl listę klientów")
        print("3. Dodaj wizytę")
        print("4. Wyświetl wszystkie wizyty")
        print("5. Wyświetl wizyty konkretnego pacjenta")
        print("6. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3/4/5/6): ")

        if wybor == '1':
            pod_wybor = input("Czy chcesz dodać nowego klienta (D) czy zaktualizować dane istniejącego klienta (A)? (D/A): ").upper()
            if pod_wybor == 'D':
                dodaj_klienta(klienci, plik)
            elif pod_wybor == 'A':
                aktualizuj_klienta(klienci, plik)
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor == '2':
            wyswietl_liste_klientow(klienci)
        elif wybor == '3':
            wizyta = dodaj_wizyte(klienci)
            if wizyta:
                zapisz_wizyte(wizyta, plik_wizyt)
                print("Dodano nową wizytę")
        elif wybor == '4':
            wyswietl_wszystkie_wizyty(plik_wizyt)
        elif wybor == '5':
            id_pacjenta = input("Podaj ID pacjenta: ")
            wyswietl_wizyty_pacjenta(plik_wizyt, id_pacjenta)
        elif wybor == '6':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
 