from main import przeliczanie_ceny

def test_przeliczanie_ceny():
    # Sprawdzenie poprawnosci obliczen
    assert przeliczanie_ceny(100) == 123, "Błąd: nieprawidłowe obliczenie ceny brutto dla 100"
    assert przeliczanie_ceny(200) == 246, "Błąd: nieprawidłowe obliczenie ceny brutto dla 200"

test_przeliczanie_ceny()