from main import generuj_id_zwierzecia, przeliczanie_ceny, wczytaj_dane, znajdz_klienta_po_id
import json
import os
from unittest.mock import patch, mock_open

# Test dla funkcji przeliczanie_ceny
def test_przeliczanie_ceny():
    # Sprawdzenie poprawnosci obliczen
    assert przeliczanie_ceny(100) == 123, "Błąd: nieprawidłowe obliczenie ceny brutto dla 100"
    assert przeliczanie_ceny(200) == 246, "Błąd: nieprawidłowe obliczenie ceny brutto dla 200"

# Test dla funkcji wczytaj_dane
def test_wczytaj_dane():
    # Test, gdy plik nie istnieje
    with patch('os.path.exists', return_value=False):
        assert wczytaj_dane("nieistniejacy_plik.json") == [], "Błąd: powinno zwrócić pustą listę, gdy plik nie istnieje"
    
    # Test, gdy plik istnieje i jest poprawny
    sample_data = [{"id_zwierzecia": "001"}]
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data=json.dumps(sample_data))):
            assert wczytaj_dane("istniejacy_plik.json") == sample_data, "Błąd: powinno zwrócić dane z pliku"

    # Test, gdy plik istnieje, ale zawiera błędne dane JSON
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_open(read_data="niepoprawny json")):
            assert wczytaj_dane("bledny_plik.json") == [], "Błąd: powinno zwrócić pustą listę dla błędnego JSON"

# Test dla funkcji generuj_id_zwierzecia
def test_generuj_id_zwierzecia():
    # Test, gdy lista jest pusta
    assert generuj_id_zwierzecia([]) == '001', "Błąd: powinno zwrócić '001' dla pustej listy"
    
    # Test, gdy lista zawiera elementy
    klienci = [{'id_zwierzecia': '001'}, {'id_zwierzecia': '002'}]
    assert generuj_id_zwierzecia(klienci) == '003', "Błąd: powinno zwrócić '003' jako kolejne ID"

# Test dla funkcji znajdz_klienta_po_id
def test_znajdz_klienta_po_id():
    klienci = [{'id_zwierzecia': '001'}, {'id_zwierzecia': '002'}]
    # Test, gdy klient jest znaleziony
    assert znajdz_klienta_po_id(klienci, '001') == {'id_zwierzecia': '001'}, "Błąd: powinno zwrócić klienta z ID '001'"
    # Test, gdy klient nie jest znaleziony
    assert znajdz_klienta_po_id(klienci, '003') is None, "Błąd: powinno zwrócić None, gdy ID nie istnieje"

# Wywołanie testów
test_wczytaj_dane()
test_generuj_id_zwierzecia()
test_znajdz_klienta_po_id()
test_przeliczanie_ceny()