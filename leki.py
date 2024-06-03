import json
import os
import re

LEKI_FILE_PATH = os.path.join(os.path.dirname(__file__), 'leki.json')

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

def waliduj_ilosc(ilosc):
    pattern = r'^\d+\s*\w*$'
    if re.match(pattern, ilosc):
        return True
    return False

def dodaj_lek():
    leki = wczytaj_leki()

    nazwa = input("Podaj nazwę leku: ").strip()
    while not nazwa:
        print("Nazwa leku nie może być pusta.")
        nazwa = input("Podaj nazwę leku: ").strip()
    
    if nazwa in leki:
        print("Lek już istnieje w bazie.")
        return

    while True:
        ilosc = input("Podaj ilość (np. 10 opakowań): ").strip()
        if waliduj_ilosc(ilosc):
            if re.match(r'^\d+$', ilosc):
                potwierdzenie = input(f"Wpisałeś tylko {ilosc}. Czy na pewno chcesz zapisać tylko tę liczbę? (tak/nie): ").strip().lower()
                if potwierdzenie == 'tak':
                    break
            else:
                break
        print("Nieprawidłowa ilość. Podaj ilość w formacie liczba jednostka (np. 10 opakowań).")

    dostawca = input("Podaj dostawcę: ").strip()
    while not dostawca:
        print("Dostawca nie może być pusty.")
        dostawca = input("Podaj dostawcę: ").strip()

    leki[nazwa] = {
        "ilosc": ilosc,
        "dostawca": dostawca
    }
    zapisz_leki(leki)
    print(f"Lek {nazwa} został dodany do bazy danych.")

def usun_lek():
    leki = wczytaj_leki()
    nazwa = input("Podaj nazwę leku do usunięcia: ").strip()

    if nazwa in leki:
        del leki[nazwa]
        zapisz_leki(leki)
        print(f"Lek {nazwa} został usunięty z bazy danych.")
    else:
        print("Lek nie istnieje w bazie.")

def edytuj_lek():
    leki = wczytaj_leki()
    nazwa = input("Podaj nazwę leku do edytowania: ").strip()
    dokladny_wybor = input("Czy chcesz edytować ilość leku (I) czy zmienić dostawcę leku (D)? (I/D): ").strip().upper()
    if dokladny_wybor == 'I':
        if nazwa in leki:
            nowa_ilosc_input = input(f"Podaj nową ilość dla {nazwa}: ").strip()
            try:
                nowa_ilosc = int(nowa_ilosc_input)
            except ValueError:
                print("Nieprawidłowa ilość. Proszę podać liczbę.")
                return
            leki[nazwa]["ilosc"] = nowa_ilosc
            zapisz_leki(leki)
            print(f"Ilość leku {nazwa} została zaktualizowana.")
        else:
            print("Lek nie istnieje w bazie.")
    elif dokladny_wybor == 'D':
        if nazwa in leki:
            nowy_dostawca = input(f"Podaj nowego dostawcę: ").strip()
            leki[nazwa]["dostawca"] = nowy_dostawca
            zapisz_leki(leki)
            print(f"Dostawca leku {nazwa} został zaktualizowany.")
        else:
            print("Wystąpił błąd.")
    else:
        print("Nieprawidłowy wybór, spróbuj ponownie.")
    
def wyswietl_wszystkie_leki():
    leki = wczytaj_leki()
    if not leki:
        print("Brak leków w bazie danych.")
    else:
        print("Aktualna lista leków:")
        for nazwa, dane in leki.items():
            print(f"Nazwa: {nazwa}, Ilość: {dane['ilosc']}, Dostawca: {dane['dostawca']}")
