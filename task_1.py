import math         # https://docs.python.org/3/library/math.html
import random       # https://docs.python.org/3/library/random.html
import time         # https://docs.python.org/3/library/time.html

def generuj_losowe_dane(rozmiar=5):
    """Generuje losowe dane numeryczne i tekstowe."""
    liczby = [random.randint(0, 100) for _ in range(rozmiar)]                 # https://docs.python.org/3/library/random.html#random.randint
    litery = [chr(random.randint(65, 90)) for _ in range(rozmiar)]            # https://docs.python.org/3/library/random.html#random.randint
    return liczby, litery

def polacz_listy(lista1, lista2):
    """Łączy dwie listy w pary."""
    return list(zip(lista1, lista2))                                         # https://docs.python.org/3/library/functions.html#zip

def przetworz_dane(dane):
    """Sortuje dane i oblicza pierwiastki kwadratowe liczb."""
    posortowane_dane = sorted(dane)                                          # https://docs.python.org/3/library/functions.html#sorted
    pierwiastki = [math.sqrt(x) if x > 0 else None for x in posortowane_dane] # https://docs.python.org/3/library/math.html#math.sqrt
    return posortowane_dane, pierwiastki

def bezpieczne_dzielenie(liczby):
    """Wykonuje pojedynczą operację dzielenia z obsługą błędów."""
    if len(liczby) < 2:
        return ['Za mało liczb do dzielenia.']
    
    a, b = random.sample(liczby, 2)                                          # https://docs.python.org/3/library/random.html#random.sample

    try:
        # Sprawdzenie typów dla TypeError
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))): # https://docs.python.org/3/library/functions.html#isinstance
            raise TypeError('Nieprawidłowy typ danych do dzielenia.')
        
        wynik = a / b
        return [f'{a} / {b} = {wynik:.2f}']
    except ZeroDivisionError:                                                # https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
        return [f'{a} / {b} = Dzielenie przez zero.']
    except TypeError as e:                                                   # https://docs.python.org/3/library/exceptions.html#TypeError
        return [f'Błąd typu: {e}']
    
def main():
    start_time = time.time()                                                 # https://docs.python.org/3/library/time.html#time.time
    # Generowanie losowych danych
    liczby, litery = generuj_losowe_dane()
    print('Liczby:', liczby)
    print('Litery:', litery)

    # Łączenie list w pary
    polaczone_dane = polacz_listy(liczby, litery)
    print('Połączone pary:', polaczone_dane)

    # Przetwarzanie danych numerycznych (sortowanie i obliczanie pierwiastków)
    posortowane_liczby, pierwiastki = przetworz_dane(liczby)
    print('Posortowane liczby:', posortowane_liczby)
    print('Pierwiastki kwadratowe:', pierwiastki)

    # Wykonanie losowej operacji dzielenia
    wynik_dzielenia = bezpieczne_dzielenie(posortowane_liczby)
    print('Wynik dzielenia (poprawne dane):', wynik_dzielenia[0])

    # Testowanie obsługi ZeroDivisionError
    dane_z_zerem = [10, 0, 20, 5]  # Lista zawierająca zero
    print('Testowanie obsługi ZeroDivisionError:')
    wynik_dzielenia = bezpieczne_dzielenie(dane_z_zerem)
    print('Wynik dzielenia (dzielenie przez zero):', wynik_dzielenia[0])

    # Testowanie obsługi TypeError
    dane_z_bledem_typu = ['10', 20, 5]  # Lista zawierająca ciąg znaków
    print('Testowanie obsługi TypeError:')
    wynik_dzielenia = bezpieczne_dzielenie(dane_z_bledem_typu)
    print('Wynik dzielenia (błąd typu):', wynik_dzielenia[0])

    # Obliczenie rzeczywistego czasu wykonania
    czas_wykonania = time.time() - start_time
    print(f'Czas wykonania: {czas_wykonania:.5f} sekund')

if __name__ == '__main__':
    main()
