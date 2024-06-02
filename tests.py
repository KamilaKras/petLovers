import io
import json
import os
from unittest.mock import patch, mock_open
import clients
import visits
import data

# Test dla funkcji przeliczanie_ceny
def test_przeliczanie_ceny():
    # Sprawdzenie poprawnosci obliczen
    assert visits.przeliczanie_ceny(100) == 123, "Błąd: nieprawidłowe obliczenie ceny brutto dla 100"
    assert visits.przeliczanie_ceny(200) == 246, "Błąd: nieprawidłowe obliczenie ceny brutto dla 200"

# Test dla funkcji wczytaj_dane
def test_wczytaj_dane():
    # Test, gdy plik nie istnieje
    with patch('os.path.exists', return_value=False):
        assert data.wczytaj_dane("nieistniejacy_plik.json") == [], "Błąd: powinno zwrócić pustą listę, gdy plik nie istnieje"
    
    # Test, gdy plik istnieje i jest poprawny
    sample_data = [{"id_zwierzecia": "001"}]
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json.dumps(sample_data))):
            assert data.wczytaj_dane("istniejacy_plik.json") == sample_data, "Błąd: powinno zwrócić dane z pliku"

    # Test, gdy plik istnieje, ale zawiera błędne dane JSON
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="niepoprawny json")):
            assert data.wczytaj_dane("bledny_plik.json") == [], "Błąd: powinno zwrócić pustą listę dla błędnego JSON"

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
    
    user_inputs = ['19.02.2019', '001', 'katar', 'aspiryna', '100']
    expected_output = {
        'Data wizyty': '19.02.2019', 
        'Pacjent': '001', 
        'Choroba': 'katar', 
        'Leki': 'aspiryna', 
        'Cena netto': 100.0, 
        'Cena brutto': 123.0
    }
    
    with patch('builtins.input', side_effect=user_inputs), patch('clients.znajdz_klienta_po_id', return_value=klienci[0]):
        result = visits.dodaj_wizyte(klienci)
        assert result == expected_output, "Test failed: dodaj_wizyte did not return expected dictionary."

# Test dla funkcji zapisz_wizyte
def test_zapisz_wizyte():
    wizyta = {
        'Data wizyty': '20.02.2019', 
        'Pacjent': '002', 
        'Choroba': 'grypa', 
        'Leki': 'ibuprofen', 
        'Cena netto': 150, 
        'Cena brutto': 184.5
    }
    plik_wizyt = 'wizyty.json'
    mock_file = mock_open(read_data="")  # Symuluj pusty plik

    with patch('builtins.open', mock_file), patch('os.path.exists', return_value=True):
        visits.zapisz_wizyte(wizyta, plik_wizyt)

        mock_file.assert_any_call(plik_wizyt, 'w')
        mock_file.assert_any_call(plik_wizyt, 'r')

        assert mock_file().write.called, "Nie wywołano metody write."

# Test dla funkcji wyswietl_wszystkie_wizyty
def test_wyswietl_wszystkie_wizyty():
    sample_data = {
        '1': {'Data wizyty': '20.02.2019', 'Pacjent': '001', 'Choroba': 'grypa', 'Leki': 'ibuprofen', 'Cena brutto': 184.5}
    }
    expected_output = "Wszystkie zarejestrowane wizyty:\nWizyta ID: 1, Data: 20.02.2019, Pacjent ID: 001, Choroba: grypa, Leki: ibuprofen, Cena brutto: 184.5\n"
    
    mock_file = mock_open(read_data=json.dumps(sample_data))
    with patch('builtins.open', mock_file), patch('sys.stdout', new=io.StringIO()) as fake_out:
        visits.wyswietl_wszystkie_wizyty('wizyty.json')
        assert fake_out.getvalue() == expected_output, "Test failed: Output not as expected."

# Test dla funkcji wyswietl_wizyty_pacjenta
def test_wyswietl_wizyty_pacjenta():
    sample_data = {
        '1': {'Data wizyty': '20.02.2019', 'Pacjent': '001', 'Choroba': 'grypa', 'Leki': 'ibuprofen', 'Cena brutto': 184.5},
        '2': {'Data wizyty': '21.02.2019', 'Pacjent': '002', 'Choroba': 'katar', 'Leki': 'paracetamol', 'Cena brutto': 123.0}
    }
    expected_output = "Wizyty dla pacjenta o ID 001:\nWizyta ID: 1, Data: 20.02.2019, Choroba: grypa, Leki: ibuprofen, Cena brutto: 184.5\n"
    
    mock_file = mock_open(read_data=json.dumps(sample_data))
    with patch('builtins.open', mock_file), patch('sys.stdout', new=io.StringIO()) as fake_out:
        visits.wyswietl_wizyty_pacjenta('wizyty.json', '001')
        assert fake_out.getvalue() == expected_output, "Test failed: Output for specific patient not as expected."

# Wywołanie testów
test_wczytaj_dane()
test_generuj_id_zwierzecia()
test_znajdz_klienta_po_id()
test_przeliczanie_ceny()
test_dodaj_wizyte()
test_zapisz_wizyte()
test_wyswietl_wszystkie_wizyty()
test_wyswietl_wizyty_pacjenta()