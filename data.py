import json
import os

def wczytaj_dane(plik):
    try:
        with open(plik, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Błąd dekodowania pliku JSON.")
        return []
    except UnicodeDecodeError:
        print("Błąd dekodowania pliku. Upewnij się, że plik jest zapisany w kodowaniu UTF-8.")
        return []

def zapisz_dane(plik, dane):
    with open(plik, 'w') as file:
        json.dump(dane, file, indent=4)
