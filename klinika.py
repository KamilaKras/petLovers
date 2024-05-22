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

def generuj_id_zwierzecia(zwierzeta):
    if not zwierzeta:
        return '001'
    ids = [int(z['id']) for z in zwierzeta]
    return str(max(ids) + 1).zfill(3)

def czy_zwierze_istnieje(zwierzeta, imie_zwierzecia, wiek_zwierzecia, imie_wlasciciela):
    for z in zwierzeta:
        if (z['imie_zwierzecia'] == imie_zwierzecia and
            z['wiek_zwierzecia'] == wiek_zwierzecia and
            z['imie_wlasciciela'] == imie_wlasciciela):
            return True
    return False

def dodaj_zwierze(zwierzeta, id_zwierzecia, imie_zwierzecia, wiek_zwierzecia, imie_wlasciciela):
    zwierzeta.append({
        "id": id_zwierzecia,
        "imie_zwierzecia": imie_zwierzecia,
        "wiek_zwierzecia": wiek_zwierzecia,
        "imie_wlasciciela": imie_wlasciciela
    })

def main():
    plik = 'zwierzeta.json'
    zwierzeta = wczytaj_dane(plik)

    # Dane wejściowe od użytkownika
    imie_zwierzecia = input("Podaj imię zwierzęcia: ")
    wiek_zwierzecia = input("Podaj wiek zwierzęcia: ")
    imie_wlasciciela = input("Podaj imię właściciela: ")

    if czy_zwierze_istnieje(zwierzeta, imie_zwierzecia, wiek_zwierzecia, imie_wlasciciela):
        print(f"Zwierzę {imie_zwierzecia} o właścicielu {imie_wlasciciela} już istnieje w bazie danych.")
    else:
        id_zwierzecia = generuj_id_zwierzecia(zwierzeta)
        dodaj_zwierze(zwierzeta, id_zwierzecia, imie_zwierzecia, wiek_zwierzecia, imie_wlasciciela)
        zapisz_dane(plik, zwierzeta)
        print(f"Zwierzę {imie_zwierzecia} zostało dodane do bazy danych z ID {id_zwierzecia}.")

if __name__ == "__main__":
    main()
