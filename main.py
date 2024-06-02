import json
import os
import clients
from leki import dodaj_lek, edytuj_lek, usun_lek, wyswietl_wszystkie_leki
import visits
import data

def main():
    plik = 'clients.json'
    klienci = data.wczytaj_dane(plik)
    plik_wizyt = 'wizyty.json'

    while True:
        print("\n1. Dodaj/Zaktualizuj dane klienta")
        print("2. Wyświetl listę klientów")
        print("3. Znajdź pacjenta, wyświetl wizyty i dodaj wizytę")
        print("4. Znajdź po mikroczipie")
        print("5. Wyświetl wszystkie wizyty")
        print("6. Dodaj nową wizytę dla dowolnego pacjenta")
        print("7. Dodaj lek")
        print("8. Usuń lek")
        print("9. Edytuj lek")
        print("10. Wyświetl aktualny stan magazynowy leków")
        print("11. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3/4/5/6/7/8/9/10/11): ").strip()

        if wybor == '1':
            pod_wybor = input("Czy chcesz dodać nowego klienta (D) czy zaktualizować dane istniejącego klienta (A)? (D/A): ").strip().upper()
            if pod_wybor == 'D':
                clients.dodaj_klienta(klienci, plik)
            elif pod_wybor == 'A':
                clients.aktualizuj_klienta(klienci, plik)
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor == '2':
            clients.wyswietl_liste_klientow(klienci)
        elif wybor == '3':
            znaleziony_klient = clients.wyszukaj_pacjenta(klienci)
            if znaleziony_klient:
                print("Wybierz opcję:\n1. Dodaj wizytę\n2. Wyświetl wszystkie wizyty pacjenta")
                pod_wybor = input("Wybierz opcję (1/2): ").strip()
                if pod_wybor == '1':
                    wizyta = visits.dodaj_wizyte(klienci, znaleziony_klient['id_zwierzecia'])
                    if wizyta:
                        visits.zapisz_wizyte(wizyta, plik_wizyt)
                        print("Dodano nową wizytę")
                elif pod_wybor == '2':
                    id_pacjenta = znaleziony_klient['id_zwierzecia']
                    visits.wyswietl_wizyty_pacjenta(plik_wizyt, id_pacjenta)
                else:
                    print("Nieprawidłowy wybór, spróbuj ponownie.")
        elif wybor == '4':
            numer_mikroczipa = input("Podaj numer mikroczipa: ").strip()
            clients.wyszukaj_po_mikroczipie(klienci, numer_mikroczipa)
        elif wybor == '5':
            visits.wyswietl_wszystkie_wizyty(plik_wizyt)
        elif wybor == '6':
            wizyta = visits.dodaj_wizyte()
            visits.zapisz_wizyte(wizyta)
        elif wybor == '7':
            dodaj_lek()
        elif wybor == '8':
            usun_lek()
        elif wybor == '9':
            edytuj_lek()
        elif wybor == '10':
            wyswietl_wszystkie_leki()
        elif wybor == '11':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()

 
