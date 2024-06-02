import json
import os
import clients
import visits
import data

def main():
    plik = 'clients.json'
    klienci = data.wczytaj_dane(plik)
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
                clients.dodaj_klienta(klienci, plik)
            elif pod_wybor == 'A':
                clients.aktualizuj_klienta(klienci, plik)
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
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
 