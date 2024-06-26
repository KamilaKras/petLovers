import io
import json
import os
import sys
import clients
from leki import dodaj_lek, edytuj_lek, usun_lek, wyswietl_wszystkie_leki
import visits
import data

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

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
        print("6. Dodaj lek")
        print("7. Usuń lek")
        print("8. Edytuj lek")
        print("9. Wyświetl aktualny stan magazynowy leków")
        print("10. Zakończ działanie programu")
        wybor = input("Wybierz opcję (1/2/3/4/5/6/7/8/9/10): ").strip()

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
            klient = clients.znajdz_klienta_po_mikroczipie(klienci, numer_mikroczipa)
            if klient:
                print(f"Znaleziono klienta: ID: {klient['id_zwierzecia']}, Imię: {klient['imie']}, Nazwisko: {klient['nazwisko']}, "
                    f"Email: {klient['email']}, Telefon: {klient['telefon']}, "
                    f"Zwierzę: {klient['zwierze']['imie_zwierzecia']}, Data urodzenia: {klient['zwierze']['data_urodzenia']}, "
                    f"Typ: {klient['zwierze']['typ_zwierzecia']}, Płeć: {klient['zwierze']['plec_zwierzecia']}, Rasa: {klient['zwierze']['rasa']}")
            else:
                print("Nie znaleziono klienta z podanym numerem mikroczipa.")
        elif wybor == '5':
            visits.wyswietl_wszystkie_wizyty(plik_wizyt)
        elif wybor == '6':
            dodaj_lek()
        elif wybor == '7':
            usun_lek()
        elif wybor == '8':
            edytuj_lek()
        elif wybor == '9':
            wyswietl_wszystkie_leki()
        elif wybor == '10':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()
