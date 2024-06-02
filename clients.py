import data
import datetime

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

def znajdz_klienta_po_imieniu_zwierzaka(klienci, imie_zwierzecia):
    znalezione_zwierzaki = []
    for klient in klienci:
        if klient['zwierze']['imie_zwierzecia'] == imie_zwierzecia:
            znalezione_zwierzaki.append(klient)
    return znalezione_zwierzaki

def oblicz_wiek(data_urodzenia):
    try:
        dzisiaj = datetime.date.today()
        urodziny = datetime.datetime.strptime(data_urodzenia, '%d.%m.%Y').date()

        if urodziny > dzisiaj:
            raise ValueError

        wiek = dzisiaj.year - urodziny.year - ((dzisiaj.month, dzisiaj.day) < (urodziny.month, urodziny.day))
        return wiek

    except ValueError:
        return f"nieprawidłowa data - {data_urodzenia}"
    
def znajdz_klienta_po_mikroczipie(klienci, numer_mikroczipa):
    for klient in klienci:
        if 'numer_mikroczipa' in klient['zwierze'] and klient['zwierze']['numer_mikroczipa'] == numer_mikroczipa:
            return klient
    return None

def sprawdzenie_numeru_mikroczipa(klienci):
    while True:
        numer_mikroczipa = input("Podaj unikalny numer mikroczipa zwierzęcia: ")
        if not numer_mikroczipa.isdigit() or len(numer_mikroczipa) != 15:
            print("Numer mikroczipa musi być 15-cyfrowym ciągiem znaków.")
            continue
        
        if znajdz_klienta_po_mikroczipie(klienci, numer_mikroczipa):
            print(f"Zwierzę z numerem mikroczipa {numer_mikroczipa} już istnieje w bazie danych.")
            continue
        
        return numer_mikroczipa

def dodaj_klienta(klienci, plik):
    id_zwierzecia = generuj_id_zwierzecia(klienci)
    imie = input("Podaj imię właściciela: ")
    nazwisko = input("Podaj nazwisko właściciela: ")
    email = input("Podaj email właściciela: ")
    telefon = input("Podaj telefon właściciela: ")
    imie_zwierzecia = input("Podaj imię zwierzęcia: ")
    data_urodzenia_zwierzecia = input("Podaj datę urodzenia zwierzęcia (DD.MM.RRRR): ")
    typ_zwierzecia = input("Podaj typ zwierzęcia (np. kot, pies): ")
    plec_zwierzecia = input("Podaj płeć zwierzęcia (samiec/samica): ")
    rasa = input("Podaj rasę zwierzęcia: ")
    
    numer_mikroczipa = sprawdzenie_numeru_mikroczipa(klienci)

    klient = {
        "id_zwierzecia": id_zwierzecia,
        "imie": imie,
        "nazwisko": nazwisko,
        "email": email,
        "telefon": telefon,
        "zwierze": {
            "imie_zwierzecia": imie_zwierzecia,
            "data_urodzenia": data_urodzenia_zwierzecia,
            "typ_zwierzecia": typ_zwierzecia,
            "plec_zwierzecia": plec_zwierzecia,
            "rasa": rasa,
            "numer_mikroczipa": numer_mikroczipa
        }
    }
    klienci.append(klient)
    data.zapisz_dane(plik, klienci)
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
        klient['zwierze']['data_urodzenia'] = input(f"Podaj nową datę urodzenia zwierzęcia ({klient['zwierze']['data_urodzenia']}): ") or klient['zwierze']['data_urodzenia']
        klient['zwierze']['typ_zwierzecia'] = input(f"Podaj nowy typ zwierzęcia ({klient['zwierze']['typ_zwierzecia']}): ") or klient['zwierze']['typ_zwierzecia']
        klient['zwierze']['plec_zwierzecia'] = input(f"Podaj nową płeć zwierzęcia ({klient['zwierze']['plec_zwierzecia']}): ") or klient['zwierze']['plec_zwierzecia']
        klient['zwierze']['rasa'] = input(f"Podaj nową rasę zwierzęcia ({klient['zwierze']['rasa']}): ") or klient['zwierze']['rasa']
        print(f"Poprzedni numer mikroczipa: {klient['zwierze']['numer_mikroczipa']}")
        nowy_numer_mikroczipa = sprawdzenie_numeru_mikroczipa(klienci)
        klient['zwierze']['numer_mikroczipa'] = nowy_numer_mikroczipa
        
        data.zapisz_dane(plik, klienci)
        print(f"Dane klienta o ID {id_zwierzecia} zostały zaktualizowane.")
    else:
        print(f"Klient o ID {id_zwierzecia} nie został znaleziony.")

def wyszukaj_pacjenta_po_id(klienci, id_zwierzecia):
    for klient in klienci:
        if klient['id_zwierzecia'] == id_zwierzecia:
            return klient
    return None

def wyszukaj_pacjenta_po_imieniu(klienci, imie_zwierzecia):
    znalezione_zwierzaki = []
    for klient in klienci:
        if klient['zwierze']['imie_zwierzecia'] == imie_zwierzecia:
            znalezione_zwierzaki.append(klient)
    return znalezione_zwierzaki

def wyszukaj_pacjenta(klienci):
    while True:
        imie_lub_id = input("Wyszukaj pacjenta po imieniu zwierzaka lub numerze ID: ")

        if imie_lub_id.isdigit():
            klient = wyszukaj_pacjenta_po_id(klienci, imie_lub_id)
            if klient:
                zwierze = klient['zwierze']
                wiek = oblicz_wiek(zwierze['data_urodzenia'])
                print(f"Imię zwierzęcia: {klient['zwierze']['imie_zwierzecia']}, Numer ID: {klient['id_zwierzecia']}, Wiek w latach: {wiek}, Imię właściciela: {klient['imie']}, Nazwisko właściciela: {klient['nazwisko']}")
                return klient
        else:
            znalezione_zwierzaki = wyszukaj_pacjenta_po_imieniu(klienci, imie_lub_id)

            if not znalezione_zwierzaki:
                print("Nie znaleziono pacjenta.")
                kontynuuj = input("Czy chcesz spróbować ponownie? (tak/nie): ")
                if kontynuuj != 'tak':
                    return None
                else:
                    continue

            if len(znalezione_zwierzaki) == 1:
                klient = znalezione_zwierzaki[0]
                print(f"Znaleziono jednego pacjenta o podanym imieniu:")
                print(f"ID: {klient['id_zwierzecia']}, Imię zwierzęcia: {klient['zwierze']['imie_zwierzecia']}, Imię właściciela: {klient['imie']}, Nazwisko właściciela: {klient['nazwisko']}")
                return klient

            if len(znalezione_zwierzaki) > 1:
                print("Znaleziono kilku pacjentów o podanych kryteriach:")
                for klient in znalezione_zwierzaki:
                    print(f"ID: {klient['id_zwierzecia']}, Imię zwierzęcia: {klient['zwierze']['imie_zwierzecia']}, Imię właściciela: {klient['imie']}, Nazwisko właściciela: {klient['nazwisko']}")

                while True:
                    wybor = input("Wybierz numer ID pacjenta, którego chcesz wybrać: ")

                    try:
                        klient = wyszukaj_pacjenta_po_id(klienci, wybor)
                        if klient in znalezione_zwierzaki:
                            return klient
                        else:
                            print("Nieprawidłowy wybór.")
                    except ValueError:
                        print("Nieprawidłowy wybór.")
            else:
                klient = znalezione_zwierzaki[0]
                return klient

def wyszukaj_po_mikroczipie(klienci, numer_mikroczipa):
    for klient in klienci:
        if klient['zwierze']['numer_mikroczipa'] == numer_mikroczipa:
            zwierze = klient['zwierze']
            print(f"Zwierzę znalezione:\n"
                  f"ID: {klient['id_zwierzecia']}\n"
                  f"Imię zwierzęcia: {zwierze['imie_zwierzecia']}\n"
                  f"Typ: {zwierze['typ_zwierzecia']}\n"
                  f"Płeć: {zwierze['plec_zwierzecia']}\n"
                  f"Rasa: {zwierze['rasa']}\n"
                  f"Wiek w latach: {zwierze['wiek']}\n"
                  f"Właściciel: {klient['imie']} {klient['nazwisko']}\n"
                  f"Email: {klient['email']}\n"
                  f"Telefon: {klient['telefon']}")
            return
    print(f"Zwierzę o numerze mikroczipa {numer_mikroczipa} nie zostało znalezione w bazie danych.")

def wyswietl_liste_klientow(klienci):
    if not klienci:
        print("Brak klientów w bazie danych.")
    else:
        for klient in klienci:
            if isinstance(klient, dict):
                zwierze = klient['zwierze']
                wiek = oblicz_wiek(zwierze['data_urodzenia'])
                print(f"ID: {klient['id_zwierzecia']}, Imię: {klient['imie']}, Nazwisko: {klient['nazwisko']}, "
                      f"Email: {klient['email']}, Telefon: {klient['telefon']}, "
                      f"Zwierzę: {zwierze['imie_zwierzecia']}, Data urodzenia: {zwierze['data_urodzenia']}, Wiek w latach: {wiek}, Typ: {zwierze['typ_zwierzecia']}, Płeć: {zwierze['plec_zwierzecia']}, Rasa: {zwierze['rasa']}, Numer mikroczipa: {zwierze['numer_mikroczipa']}")
            else:
                print("Błąd danych: Niepoprawny format klienta, oczekiwano słownika.")
    