import json
import os

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
    dokladny_wybor = input("Czy chcesz edytować ilość leku (I) czy zmienić dostawcę leku (D)? (I/D): ").upper()
    if dokladny_wybor == 'I':
        if nazwa in leki:
            nowa_ilosc = int(input(f"Podaj nową ilość dla {nazwa}: "))
            leki[nazwa]["ilosc"] = nowa_ilosc
            zapisz_leki(leki)
            print(f"Ilość leku {nazwa} została zaktualizowana.")
        else:
            print("Lek nie istnieje w bazie.")
    elif dokladny_wybor == 'D':
        if nazwa in leki:
            nowy_dostawca = str(input(f"Podaj nowego dostawcę: "))
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