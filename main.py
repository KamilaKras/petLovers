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
def main():
    plik = 'clients.json'
    klienci = wczytaj_dane(plik)

    while True:
        print("\n1. Dodaj/Zaktualizuj dane klienta")
        print("2. Wyświetl listę klientów")
        print("3. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3): ")

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
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
    


#Funkcje do napisania:
#Obliczanie ceny brutto na podstawie ceny netto - WERONIKA
#Dodawanie pacjentów - Andrzej
#Dodawanie informacji o wizycie (kiedy, kto, co, jakie leki zapisane + cena za zabieg powiazania z obliczeniem ceny brutto) - Lena
