import datetime
import io
import json
import os
from unittest.mock import MagicMock, patch, mock_open
import clients
import visits
import data
import leki

# Test dla funkcji przeliczanie_ceny
def test_przeliczanie_ceny():
    # Sprawdzenie poprawnosci obliczen
    result1 = visits.przeliczanie_ceny(100)
    result2 = visits.przeliczanie_ceny(200)
    result3 = visits.przeliczanie_ceny("Brak danych")
    
    assert result1 == "108,00 zł", f"Błąd: nieprawidłowe obliczenie ceny brutto dla 100, wynik: {result1}"
    assert result2 == "216,00 zł", f"Błąd: nieprawidłowe obliczenie ceny brutto dla 200, wynik: {result2}"
    assert result3 == "Brak danych", f"Błąd: nieprawidłowe obliczenie ceny brutto dla 'Brak danych', wynik: {result3}"

# Test dla funkcji generuj_id_zwierzecia
def test_generuj_id_zwierzecia():
    # Test, gdy lista jest pusta
    assert clients.generuj_id_zwierzecia([]) == '001', "Błąd: powinno zwrócić '001' dla pustej listy"
    
    # Test, gdy lista zawiera elementy
    klienci = [{'id_zwierzecia': '001'}, {'id_zwierzecia': '002'}]
    assert clients.generuj_id_zwierzecia(klienci) == '003', "Błąd: powinno zwrócić '003' jako kolejne ID"

# Test dla funkcji znajdz_klienta_po_id
def test_znajdz_klienta_po_id():
    klienci = [{'id_zwierzecia': '001'}, {'id_zwierzecia': '002'}]
    # Test, gdy klient jest znaleziony
    assert clients.znajdz_klienta_po_id(klienci, '001') == {'id_zwierzecia': '001'}, "Błąd: powinno zwrócić klienta z ID '001'"
    # Test, gdy klient nie jest znaleziony
    assert clients.znajdz_klienta_po_id(klienci, '003') is None, "Błąd: powinno zwrócić None, gdy ID nie istnieje"

# Test dla funkcji dodaj_wizyte
def test_dodaj_wizyte():
    klienci = [{'id_zwierzecia': '001', 'imie': 'Jan'}]
    
    user_inputs = ['19.02.2019', 'katar', 'aspiryna', '', '', '100']
    expected_output = {
        'Data wizyty': '19.02.2019', 
        'Pacjent': '001', 
        'Choroba': 'katar', 
        'Recepta': {
            'Leki': 'aspiryna', 
            'Dawkowanie': "Brak danych"
        },
        'Dodatkowe informacje': "Brak danych",
        'Cena netto': 100.0, 
        'Cena brutto': '108,00 zł'
    }
    
    with patch('builtins.input', side_effect=user_inputs), patch('clients.znajdz_klienta_po_id', return_value=klienci[0]):
        result = visits.dodaj_wizyte(klienci, '001')
        assert result == expected_output, f"Test failed: dodaj_wizyte did not return expected dictionary. Wynik: {result}"

# Test dla funkcji zapisz_wizyte
def test_zapisz_wizyte():
    wizyta = {
        'Data wizyty': '20.02.2019', 
        'Pacjent': '002', 
        'Choroba': 'grypa', 
        'Recepta': {
            'Leki': 'ibuprofen', 
            'Dawkowanie': "Brak danych"
        },
        'Dodatkowe informacje': "Brak danych", 
        'Cena netto': 150.0, 
        'Cena brutto': '162,00 zł'
    }
    plik_wizyt = 'wizyty.json'
    mock_file = mock_open(read_data=json.dumps({}))

    with patch('builtins.open', mock_file), patch('os.path.exists', return_value=True):
        visits.zapisz_wizyte(wizyta, plik_wizyt)

        mock_file.assert_any_call(plik_wizyt, 'w', encoding='utf-8')
        mock_file.assert_any_call(plik_wizyt, 'r', encoding='utf-8')

        handle = mock_file()
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        expected_data = json.dumps({1: wizyta}, indent=4, ensure_ascii=False)
        
        assert written_data == expected_data, f"Błąd: Zapisane dane nie są zgodne z oczekiwanymi. Wynik: {written_data}"

# Test dla funkcji wyswietl_wszystkie_wizyty
def test_wyswietl_wszystkie_wizyty():
    sample_data = {
        '1': {
            'Data wizyty': '20.02.2019',
            'Pacjent': '001',
            'Choroba': 'grypa',
            'Recepta': {
                'Leki': 'ibuprofen',
                'Dawkowanie': "Brak danych"
            },
            'Dodatkowe informacje': "Brak danych",
            'Cena netto': 150.0,
            'Cena brutto': '162,00 zł'
        }
    }
    expected_output = "Wszystkie zarejestrowane wizyty:\nWizyta ID: 1, Data: 20.02.2019, Pacjent ID: 001, Choroba: grypa, Leki: ibuprofen, Dawkowanie: Brak danych, Dodatkowe informacje: Brak danych, Cena netto: 150,00 zł, Cena brutto: 162,00 zł\n"
    
    mock_file = mock_open(read_data=json.dumps(sample_data))
    with patch('builtins.open', mock_file), patch('sys.stdout', new=io.StringIO()) as fake_out:
        visits.wyswietl_wszystkie_wizyty('wizyty.json')
        assert fake_out.getvalue() == expected_output, f"Test failed: Output not as expected. Output: {fake_out.getvalue()}"


# Test dla funkcji wyswietl_wizyty_pacjenta
def test_wyswietl_wizyty_pacjenta():
    sample_data = {
        '1': {
            'Data wizyty': '20.02.2019',
            'Pacjent': '001',
            'Choroba': 'grypa',
            'Recepta': {
                'Leki': 'ibuprofen',
                'Dawkowanie': "Brak danych"
            },
            'Dodatkowe informacje': "Brak danych",
            'Cena netto': 150.0,
            'Cena brutto': '162,00 zł'
        },
        '2': {
            'Data wizyty': '21.02.2019',
            'Pacjent': '002',
            'Choroba': 'katar',
            'Recepta': {
                'Leki': 'paracetamol',
                'Dawkowanie': "Brak danych"
            },
            'Dodatkowe informacje': "Brak danych",
            'Cena netto': 123.0,
            'Cena brutto': '132,84 zł'
        }
    }
    expected_output = "Wizyty dla pacjenta o ID 001:\nWizyta ID: 1, Data: 20.02.2019, Choroba: grypa, Leki: ibuprofen, Dawkowanie: Brak danych, Dodatkowe informacje: Brak danych, Cena netto: 150,00 zł, Cena brutto: 162,00 zł\n"
    
    mock_file = mock_open(read_data=json.dumps(sample_data))
    with patch('builtins.open', mock_file), patch('sys.stdout', new=io.StringIO()) as fake_out:
        visits.wyswietl_wizyty_pacjenta('wizyty.json', '001')
        assert fake_out.getvalue() == expected_output, "Test failed: Output for specific patient not as expected."
# Test dla funkcji znajdz_klienta_po_imieniu_zwierzaka
def test_znajdz_klienta_po_imieniu_zwierzaka():
    klienci = [
        {'id_zwierzecia': '001', 'zwierze': {'imie_zwierzecia': 'Burek'}},
        {'id_zwierzecia': '002', 'zwierze': {'imie_zwierzecia': 'Azor'}},
        {'id_zwierzecia': '003', 'zwierze': {'imie_zwierzecia': 'Burek'}}
    ]
    # Test, gdy zwierzak jest znaleziony
    assert len(clients.znajdz_klienta_po_imieniu_zwierzaka(klienci, 'Burek')) == 2, "Błąd: powinno znaleźć dwóch klientów z imieniem zwierzaka 'Burek'"
    # Test, gdy zwierzak nie jest znaleziony
    assert clients.znajdz_klienta_po_imieniu_zwierzaka(klienci, 'Max') == [], "Błąd: powinno zwrócić pustą listę, gdy imię zwierzaka nie istnieje"

# Test dla funkcji oblicz_wiek
def test_oblicz_wiek():
    # Test poprawnej daty
    assert clients.oblicz_wiek('01.01.2010') == datetime.date.today().year - 2010, "Błąd: nieprawidłowe obliczenie wieku"
    # Test przyszłej daty
    assert clients.oblicz_wiek('01.01.2100') == 'nieprawidłowa data - 01.01.2100', "Błąd: przyszła data nie jest poprawna"
    # Test niepoprawnej daty
    assert 'nieprawidłowa data' in clients.oblicz_wiek('niepoprawna data'), "Błąd: niepoprawna data powinna zwrócić komunikat o błędzie"

# Test dla funkcji znajdz_klienta_po_mikroczipie
def test_znajdz_klienta_po_mikroczipie():
    klienci = [
        {'id_zwierzecia': '001', 'zwierze': {'numer_mikroczipa': '123456789012345'}},
        {'id_zwierzecia': '002', 'zwierze': {'numer_mikroczipa': '543210987654321'}}
    ]
    # Test, gdy klient jest znaleziony
    assert clients.znajdz_klienta_po_mikroczipie(klienci, '123456789012345') == klienci[0], "Błąd: powinno znaleźć klienta z numerem mikroczipa '123456789012345'"
    # Test, gdy klient nie jest znaleziony
    assert clients.znajdz_klienta_po_mikroczipie(klienci, '000000000000000') is None, "Błąd: powinno zwrócić None, gdy numer mikroczipa nie istnieje"

# Test dla funkcji sprawdzenie_numeru_mikroczipa
def test_sprawdzenie_numeru_mikroczipa():
    klienci = [
        {'id_zwierzecia': '001', 'zwierze': {'numer_mikroczipa': '123456789012345'}}
    ]
    # Test poprawnego numeru mikroczipa
    with patch('builtins.input', side_effect=['543210987654321']):
        assert clients.sprawdzenie_numeru_mikroczipa(klienci) == '543210987654321', "Błąd: powinno zwrócić podany numer mikroczipa"
    # Test numeru mikroczipa, który już istnieje
    with patch('builtins.input', side_effect=['123456789012345', '543210987654321']):
        assert clients.sprawdzenie_numeru_mikroczipa(klienci) == '543210987654321', "Błąd: powinno zwrócić nowy numer mikroczipa, ponieważ pierwszy już istnieje"
    # Test niepoprawnego numeru mikroczipa
    with patch('builtins.input', side_effect=['123', '543210987654321']):
        assert clients.sprawdzenie_numeru_mikroczipa(klienci) == '543210987654321', "Błąd: powinno zwrócić poprawny numer mikroczipa po podaniu niepoprawnego"
# Test dla funkcji usun_znaki_diakrytyczne
def test_usun_znaki_diakrytyczne():
    assert clients.usun_znaki_diakrytyczne('Łucja') == 'lucja', "Błąd: nieprawidłowe usunięcie znaków diakrytycznych"
    assert clients.usun_znaki_diakrytyczne('Śląsk') == 'slask', "Błąd: nieprawidłowe usunięcie znaków diakrytycznych"
    assert clients.usun_znaki_diakrytyczne('Café') == 'cafe', "Błąd: nieprawidłowe usunięcie znaków diakrytycznych"

# Test dla funkcji dodaj_klienta
def test_dodaj_klienta():
    klienci = []
    user_inputs = [
        'Jan', 'Kowalski', 'jan.kowalski@example.com', '123456789', 
        'Burek', '01.01.2015', 'Pies', 'Samiec', 'Owczarek', '123456789012345'
    ]
    expected_output = {
        'id_zwierzecia': '001',
        'imie': 'Jan',
        'nazwisko': 'Kowalski',
        'email': 'jan.kowalski@example.com',
        'telefon': '123456789',
        'zwierze': {
            'imie_zwierzecia': 'Burek',
            'data_urodzenia': '01.01.2015',
            'typ_zwierzecia': 'Pies',
            'plec_zwierzecia': 'samiec',
            'rasa': 'Owczarek',
            'numer_mikroczipa': '123456789012345'
        }
    }
    with patch('builtins.input', side_effect=user_inputs), patch('data.zapisz_dane') as mock_zapisz_dane:
        clients.dodaj_klienta(klienci, 'clients.json')
        assert klienci[0] == expected_output, f"Błąd: dodaj_klienta nie zwróciło oczekiwanego słownika. Wynik: {klienci[0]}"

# Test dla funkcji aktualizuj_klienta
def test_aktualizuj_klienta():
    klienci = [{
        'id_zwierzecia': '001',
        'imie': 'Jan',
        'nazwisko': 'Kowalski',
        'email': 'jan.kowalski@example.com',
        'telefon': '123456789',
        'zwierze': {
            'imie_zwierzecia': 'Burek',
            'data_urodzenia': '01.01.2015',
            'typ_zwierzecia': 'Pies',
            'plec_zwierzecia': 'samiec',
            'rasa': 'Owczarek',
            'numer_mikroczipa': '123456789012345'
        }
    }]
    user_inputs = ['001', 'Janusz', '', '', '', '', '', '', '', '', '']
    expected_output = {
        'id_zwierzecia': '001',
        'imie': 'Janusz',
        'nazwisko': 'Kowalski',
        'email': 'jan.kowalski@example.com',
        'telefon': '123456789',
        'zwierze': {
            'imie_zwierzecia': 'Burek',
            'data_urodzenia': '01.01.2015',
            'typ_zwierzecia': 'Pies',
            'plec_zwierzecia': 'samiec',
            'rasa': 'Owczarek',
            'numer_mikroczipa': '123456789012345'
        }
    }
    with patch('builtins.input', side_effect=user_inputs), patch('data.zapisz_dane') as mock_zapisz_dane:
        clients.aktualizuj_klienta(klienci, 'clients.json')
        assert klienci[0] == expected_output, f"Błąd: aktualizuj_klienta nie zaktualizowało poprawnie klienta. Wynik: {klienci[0]}"

# Test dla funkcji normalizuj_id
def test_normalizuj_id():
    assert clients.normalizuj_id('1') == '001', "Błąd: niepoprawna normalizacja ID dla '1'"
    assert clients.normalizuj_id('12') == '012', "Błąd: niepoprawna normalizacja ID dla '12'"
    assert clients.normalizuj_id('123') == '123', "Błąd: niepoprawna normalizacja ID dla '123'"

# Test dla funkcji waliduj_date
def test_waliduj_date():
    assert visits.waliduj_date('01.01.2020') == datetime.datetime(2020, 1, 1), "Błąd: powinno zwrócić datę 01.01.2020"
    assert visits.waliduj_date('32.01.2020') is None, "Błąd: nieprawidłowa data powinna zwrócić None"
    assert visits.waliduj_date('01-01-2020') is None, "Błąd: nieprawidłowy format daty powinien zwrócić None"

# Test dla funkcji zamien_none_na_brak_danych
def test_zamien_none_na_brak_danych():
    assert visits.zamien_none_na_brak_danych(None) == "Brak danych", "Błąd: powinno zwrócić 'Brak danych' dla None"
    assert visits.zamien_none_na_brak_danych("None") == "Brak danych", "Błąd: powinno zwrócić 'Brak danych' dla 'None'"
    assert visits.zamien_none_na_brak_danych("Dane") == "Dane", "Błąd: powinno zwrócić 'Dane' dla 'Dane'"

# Test dla funkcji formatuj_cene
def test_formatuj_cene():
    assert visits.formatuj_cene(100) == "100,00 zł", "Błąd: niepoprawne formatowanie ceny dla 100"
    assert visits.formatuj_cene(123.456) == "123,46 zł", "Błąd: niepoprawne formatowanie ceny dla 123.456"
    assert visits.formatuj_cene("Brak danych") == "Brak danych", "Błąd: powinno zwrócić 'Brak danych' dla 'Brak danych'"

# Test dla funkcji wczytaj_leki
def test_wczytaj_leki():
    # Test, gdy plik nie istnieje
    with patch('os.path.exists', return_value=False):
        assert leki.wczytaj_leki() == {}, "Błąd: powinno zwrócić pusty słownik, gdy plik nie istnieje"

    # Test, gdy plik istnieje i jest poprawny
    sample_data = {"Paracetamol": {"ilosc": "10 opakowań", "dostawca": "Firma A"}}
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json.dumps(sample_data))):
            assert leki.wczytaj_leki() == sample_data, "Błąd: powinno zwrócić dane z pliku"

    # Test, gdy plik istnieje, ale zawiera błędne dane JSON
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="niepoprawny json")):
            assert leki.wczytaj_leki() == {}, "Błąd: powinno zwrócić pusty słownik dla błędnego JSON"

# Test dla funkcji zapisz_leki
def test_zapisz_leki():
    leki_data = {"Paracetamol": {"ilosc": "10 opakowań", "dostawca": "Firma A"}}
    mock_file = mock_open()

    with patch('builtins.open', mock_file):
        leki.zapisz_leki(leki_data)

        mock_file.assert_any_call(leki.LEKI_FILE_PATH, 'w')
        handle = mock_file()
        written_data = "".join(call.args[0] for call in handle.write.call_args_list)
        expected_data = json.dumps(leki_data, indent=4)
        
        assert written_data == expected_data, f"Błąd: Zapisane dane nie są zgodne z oczekiwanymi. Wynik: {written_data}"

# Test dla funkcji waliduj_ilosc
def test_waliduj_ilosc():
    assert leki.waliduj_ilosc('10 opakowań') is True, "Błąd: powinno zwrócić True dla '10 opakowań'"
    assert leki.waliduj_ilosc('5') is True, "Błąd: powinno zwrócić True dla '5'"
    assert leki.waliduj_ilosc('opakowań 10') is False, "Błąd: powinno zwrócić False dla 'opakowań 10'"
    assert leki.waliduj_ilosc('10opakowań') is True, "Błąd: powinno zwrócić True dla '10opakowań'"

# Test dla funkcji dodaj_lek
def test_dodaj_lek():
    leki_data = {}
    user_inputs = ['Witamina Ę', '10 opakowań', 'Dostawca A']
    expected_output = {
        'Witamina Ę': {
            'ilosc': '10 opakowań',
            'dostawca': 'Dostawca A'
        }
    }
    
    with patch('builtins.input', side_effect=user_inputs), patch('leki.wczytaj_leki', return_value=leki_data), patch('leki.zapisz_leki') as mock_zapisz:
        leki.dodaj_lek()
        mock_zapisz.assert_called_once_with(expected_output)

# Test dla funkcji usun_lek
def test_usun_lek():
    leki_data = {
        'Witamina Ę': {
            'ilosc': '10 opakowań',
            'dostawca': 'Dostawca A'
        }
    }
    user_inputs = ['Witamina e', 'tak']
    
    with patch('builtins.input', side_effect=user_inputs), patch('leki.wczytaj_leki', return_value=leki_data), patch('leki.zapisz_leki') as mock_zapisz:
        leki.usun_lek()
        mock_zapisz.assert_called_once_with({})

# Test dla funkcji edytuj_lek
def test_edytuj_lek():
    leki_data_ilosc = {
        'Witamina Ę': {
            'ilosc': '10 opakowań',
            'dostawca': 'Dostawca A'
        }
    }
    user_inputs_ilosc = ['witamina e', 'I', '15 opakowań']
    expected_output_ilosc = {
        'Witamina Ę': {
            'ilosc': '15 opakowań',
            'dostawca': 'Dostawca A'
        }
    }
    
    leki_data_dostawca = {
        'Witamina Ę': {
            'ilosc': '10 opakowań',
            'dostawca': 'Dostawca A'
        }
    }
    user_inputs_dostawca = ['witamina e', 'D', 'Dostawca B']
    expected_output_dostawca = {
        'Witamina Ę': {
            'ilosc': '10 opakowań',
            'dostawca': 'Dostawca B'
        }
    }

    with patch('builtins.input', side_effect=user_inputs_ilosc), patch('leki.wczytaj_leki', return_value=leki_data_ilosc), patch('leki.zapisz_leki') as mock_zapisz:
        leki.edytuj_lek()
        mock_zapisz.assert_called_once_with(expected_output_ilosc)

    with patch('builtins.input', side_effect=user_inputs_dostawca), patch('leki.wczytaj_leki', return_value=leki_data_dostawca), patch('leki.zapisz_leki') as mock_zapisz:
        leki.edytuj_lek()
        mock_zapisz.assert_called_once_with(expected_output_dostawca)
        
# Test dla funkcji wyswietl_wszystkie_leki
def test_wyswietl_wszystkie_leki():
    leki_data = {"Aspiryna": {"ilosc": "10 opakowań", "dostawca": "Firma B"}}
    expected_output = "Aktualna lista leków:\nNazwa: Aspiryna, Ilość: 10 opakowań, Dostawca: Firma B\n"

    with patch('leki.wczytaj_leki', return_value=leki_data), \
         patch('sys.stdout', new=io.StringIO()) as fake_out:
        leki.wyswietl_wszystkie_leki()
        assert fake_out.getvalue() == expected_output, f"Test failed: Output not as expected. Output: {fake_out.getvalue()}"

def test_znajdz_lek():
    leki_data = {
        "Witamina Ę": {"ilosc": "10 opakowań", "dostawca": "Dostawca A"},
        "Paracetamol": {"ilosc": "20 opakowań", "dostawca": "Dostawca B"}
    }
    assert leki.znajdz_lek(leki_data, "witamina e") == "Witamina Ę", "Błąd: znalezienie leku 'witamina e' powinno zwrócić 'Witamina Ę'"
    assert leki.znajdz_lek(leki_data, "paracetamol") == "Paracetamol", "Błąd: znalezienie leku 'paracetamol' powinno zwrócić 'Paracetamol'"
    assert leki.znajdz_lek(leki_data, "aspiryna") is None, "Błąd: znalezienie nieistniejącego leku 'aspiryna' powinno zwrócić None"

# Wywołanie testów
test_generuj_id_zwierzecia()
test_znajdz_klienta_po_id()
test_przeliczanie_ceny()
test_dodaj_wizyte()
test_zapisz_wizyte()
test_wyswietl_wszystkie_wizyty()
test_wyswietl_wizyty_pacjenta()
test_znajdz_klienta_po_imieniu_zwierzaka()
test_oblicz_wiek()
test_znajdz_klienta_po_mikroczipie()
test_sprawdzenie_numeru_mikroczipa()
test_usun_znaki_diakrytyczne()
test_dodaj_klienta()
test_aktualizuj_klienta()
test_normalizuj_id()
test_waliduj_date()
test_zamien_none_na_brak_danych()
test_formatuj_cene()
test_wczytaj_leki()
test_waliduj_ilosc()
test_dodaj_lek()
test_usun_lek()
test_edytuj_lek()
test_wyswietl_wszystkie_leki()
test_znajdz_lek()