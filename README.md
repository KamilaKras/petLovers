# Zakład W dobrym domu, zdrowy zwierz! - System Zarządzania Przychodnią Weterynaryjną

![Logo Systemu](/static/logo.png)

## Opis

System do zarządzania przychodnią weterynaryjną "Zakład W dobrym domu, zdrowy zwierz!" jest przeznaczony do obsługi informacji o pacjentach, ich wizytach, przepisywanych lekach oraz do wyliczania cen brutto leków na podstawie podanych cen netto. System ten umożliwia pracownikom przychodni skuteczne i efektywne zarządzanie danymi pacjentów i ich leczeniem.

## Funkcjonalności

1. **Zarządzanie pacjentami**: Przechowywanie informacji o pacjentach, takich jak imię, gatunek, wiek, historia medyczna i inne.
2. **Zarządzanie wizytami**: Rejestrowanie szczegółów dotyczących wizyt, w tym daty, czasu, celu wizyty oraz obserwacji i wniosków z wizyty.
3. **Zarządzanie lekami**: Katalogowanie leków przepisywanych pacjentom, w tym informacje o nazwie leku, dawce, sposobie stosowania oraz cenie netto.
4. **Obliczanie cen brutto**: Automatyczne wyliczanie cen brutto leków na podstawie podanych cen netto i aktualnej stawki VAT.


## Instrukcje dla użytkownika

### Jak zacząć:
1. **Uruchomienie programu**: Uruchom skrypt klikając "Run Python File". Skrypt rozpocznie się od wczytania istniejących danych z plików JSON i pokaże menu opcji.

### Obsługa:

#### Dodawanie nowego klienta:
1. Wybierz opcję `1` z głównego menu, a następnie `D`, aby dodać nowego klienta.
2. Wprowadź wymagane informacje o właścicielu i jego zwierzęciu, takie jak imię, nazwisko, email i telefon właściciela, oraz imię, wiek, typ i rasę zwierzęcia.
3. Potwierdź dane, które zostaną automatycznie zapisane.

#### Aktualizacja danych istniejącego klienta:
1. Wybierz opcję `1`, a następnie `A`, aby zaktualizować dane istniejącego klienta.
2. Podaj ID zwierzęcia, którego dane chcesz zaktualizować.
3. Wprowadź nowe dane dla każdego z pól, które chcesz zmienić. Możesz pominąć pola, których nie chcesz aktualizować.
4. Zaktualizowane dane zostaną automatycznie zapisane.

#### Wyświetlanie listy klientów:
1. Wybierz opcję `2` z głównego menu, aby wyświetlić listę wszystkich pacjentów wraz z informacjami o ich właścicielach.

### Zarządzanie wizytami:

#### Dodawanie nowej wizyty:
1. Wybierz opcję `3` z głównego menu.
2. Podaj datę wizyty, ID pacjenta (zwierzęcia), chorobę, przepisane leki oraz cenę netto za wizytę.
3. Cena brutto zostanie automatycznie obliczona i pokazana. 
4. Informacje o wizycie zostaną zapisane.

#### Wyświetlanie wszystkich wizyt:
1. Wybierz opcję `4` z głównego menu, aby wyświetlić szczegółowe informacje o wszystkich zarejestrowanych wizytach.

#### Wyświetlanie wizyt konkretnego pacjenta:
1. Wybierz opcję `5` z głównego menu.
2. Podaj ID pacjenta, dla którego chcesz zobaczyć historię wizyt.
3. Zostaną wyświetlone wszystkie wizyty dla tego pacjenta, jeżeli takie istnieją.

### Zakończenie pracy z programem:

- Aby zakończyć działanie programu, wybierz opcję `6` z głównego menu.

## Zespół tworzący system:
1. Weronika Stasiak: https://github.com/veroniiq 
2. Elena Lukyanchuk: https://github.com/elukyanchukk 
3. Kamila Kraśniewska (PO): https://github.com/KamilaKras
4. Andrzej Jerzykiewicz: https://github.com/ajerzykiewicz
