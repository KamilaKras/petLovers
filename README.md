# Zakład W dobrym domu, zdrowy zwierz! - System Zarządzania Przychodnią Weterynaryjną

![Logo Systemu](/static/logo.png)

## Opis

System do zarządzania przychodnią weterynaryjną "Zakład W dobrym domu, zdrowy zwierz!" jest przeznaczony do obsługi informacji o pacjentach, ich wizytach, przepisywanych lekach oraz do wyliczania cen brutto leków na podstawie podanych cen netto. Pozwala na odnalezienie informacji o zwierzęciu i jego właścicielu na podstawie numeru czipa. System umożliwia również zarządzanie stanami magazynowymi leków: dodawanie, edytowanie, usuwanie i sprawdzanie aktualnego stanu. System ten umożliwia pracownikom przychodni skuteczne i efektywne zarządzanie danymi pacjentów i ich leczeniem.

## Funkcjonalności

1. **Zarządzanie pacjentami**: Przechowywanie informacji o pacjentach, takich jak imię, gatunek, wiek, historia medyczna i inne.
2. **Zarządzanie wizytami**: Rejestrowanie szczegółów dotyczących wizyt, w tym daty, czasu, celu wizyty oraz obserwacji i wniosków z wizyty.
3. **Zarządzanie przypisanymi lekami**: Katalogowanie leków przepisywanych pacjentom, w tym informacje o nazwie leku, dawce, sposobie stosowania oraz cenie netto.
4. **Obliczanie cen brutto**: Automatyczne wyliczanie cen brutto leków na podstawie podanych cen netto i aktualnej stawki VAT.
5. **Zarządzanie stanem magazynowym leków**: Dodawanie, edytowanie, usuwanie oraz wyświetlanie informacji o lekach na magazynie (nazwa leku, jego ilość i informacje o dostawcy). 


## Instrukcje dla użytkownika

### Jak zacząć:
1. **Zainstalowanie niezbędnej paczki**: W terminalu edytora kodu wpisz: pip install unidecode
2. **Ukończenie instalacji**: Poczekaj aż terminal przestanie zwracać komentarze dotyczące instalacji. Jeżeli instalacja powiodła się, przejdź do następnego etapu. Jeżeli masz problem z instalacją, skontaktuj się z zespołem informatycznym.
3. **Uruchomienie programu**: Uruchom skrypt klikając "Run Python File". Skrypt rozpocznie się od wczytania istniejących danych z plików JSON i pokaże menu opcji.

### Zarządzanie pacjentami:

#### Dodawanie nowego klienta:
1. Wybierz opcję `1` z głównego menu, a następnie `D`, aby dodać nowego klienta.
2. Wprowadź informacje o właścicielu i jego zwierzęciu, takie jak imię, nazwisko, email i telefon właściciela, oraz imię, wiek, typ i rasę zwierzęcia. Jeżeli chcesz pominąć jakieś informacje, naciśnij enter.
3. Potwierdź dane, które zostaną automatycznie zapisane.

#### Aktualizacja danych istniejącego klienta:
1. Wybierz opcję `1`, a następnie `A`, aby zaktualizować dane istniejącego klienta.
2. Podaj imię lub ID zwierzęcia, którego dane chcesz zaktualizować.
3. Wprowadź nowe dane dla każdego z pól, które chcesz zmienić. Możesz pominąć pola, których nie chcesz aktualizować.
4. Zaktualizowane dane zostaną automatycznie zapisane.

#### Wyświetlanie listy klientów:
1. Wybierz opcję `2` z głównego menu, aby wyświetlić listę wszystkich pacjentów wraz z informacjami o ich właścicielach.

#### Znajdowanie pacjenta po numerze czipa:
1. Wybierz opcję `4` z głównego menu.
2. Podaj numer czipa zwierzaka, którego chcesz znaleźć.
3. Zostaną wyświetlone informacje kontaktowe do właściciela zwierzaka, jeśli ten numer czipa istnieje w bazie danych.

### Zarządzanie informacjami o wizytach pacjenta:

#### Dodawanie nowej wizyty:
1. Wybierz opcję `3` z głównego menu.
2. Podaj imię lub ID zwierzęcia, którego dotyczy działanie.
3. Jeżeli wyszukanie pacjenta po imieniu zwróciło więcej niż jeden wynik, wybierz ID konkretnego zwierzęcia (ID będą widoczne na liście wyników wyszukiwania).
4. Wybierz opcję `1`, aby dodać informacje o wizycie pacjenta.
5. Podaj datę wizyty, chorobę, przepisane leki i ich dawkowanie, dodatkowe informacje (notatki) oraz cenę netto za wizytę.
6. Cena brutto zostanie automatycznie obliczona i wyświetlona. 
7. Informacje o wizycie zostaną zapisane.

#### Wyświetlanie wizyt konkretnego pacjenta:
1. Wybierz opcję `3` z głównego menu.
2. Podaj imię lub ID zwierzęcia, którego dotyczy działanie.
3. Jeżeli wyszukanie pacjenta po imieniu zwróciło więcej niż jeden wynik, wybierz ID konkretnego zwierzęcia (ID będą widoczne na liście wyników wyszukiwania).
4. Wybierz opcję `2`, aby wyświelić informacje o wcześniejszych wizytach pacjenta.
5. Zostaną wyświetlone wszystkie wizyty dla tego pacjenta, jeżeli takie istnieją.

#### Wyświetlanie wszystkich wizyt:
1. Wybierz opcję `5` z głównego menu, aby wyświetlić szczegółowe informacje o wszystkich zarejestrowanych wizytach.

### Zarządzanie magazynem leków:

#### Dodawanie nowego leku:
1. Wybierz opcję `6` z głównego menu.
2. Podaj nazwę leku, ilość leku oraz jego dostawce.
3. Informacje o leku zostaną zapisane.

#### Usuwanie informacji o leku:
1. Wybierz opcję `7` z głównego menu.
2. Podaj nazwę leku, który chcesz usunąć.
3. Potwierdź chęć usunięcia leku wpisując 'tak'.
4. Informacje o leku zostaną usunięte.

#### Edytowanie istniejącego leku:
1. Wybierz opcję `8` z głównego menu.
2. Podaj nazwę leku do edytowania.
3. Wybierz "I", aby zmienić ilość leku na magazynie lub "D", aby zmienić informacje o dostawcy leku.
4. Informacje o leku zostaną zapisane.

#### Wyświetlanie aktualnego stanu magazynowego leków:
1. Wybierz opcję `9` z głównego menu.
2. Informacje o lekach obecnych na magazynie zostaną wyświetlone.

### Zakończenie pracy z programem:

- Aby zakończyć działanie programu, wybierz opcję `10` z głównego menu.

## Zespół tworzący system:
1. Weronika Stasiak: https://github.com/veroniiq 
2. Elena Lukyanchuk: https://github.com/elukyanchukk 
3. Kamila Kraśniewska (PO): https://github.com/KamilaKras
4. Andrzej Jerzykiewicz: https://github.com/ajerzykiewicz
