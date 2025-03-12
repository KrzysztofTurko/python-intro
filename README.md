# *Funkcje Użytkowe w Pythonie*

## 📌 Opis
**Funkcje Użytkowe w Pythonie** to projekt zawierający zestaw podstawowych funkcji, które ułatwiają pracę z danymi w Pythonie.  
Kod został zaprojektowany w sposób modułowy, co sprawia, że jest czytelny i łatwy do rozbudowy.  

Główne funkcjonalności obejmują generowanie losowych danych, operacje matematyczne, sortowanie, obsługę wyjątków oraz mierzenie czasu wykonywania operacji.  
Projekt może posłużyć jako baza do dalszej nauki i rozwijania umiejętności programistycznych.

## ⚙ Funkcjonalności

### 🔹 1. **Generowanie losowych danych**
- Tworzy listę losowych liczb całkowitych z zakresu od 0 do 100.
- Tworzy listę losowych liter od A do Z.
- Każde uruchomienie generuje nowe wartości.

### 🔹 2. **Łączenie list za pomocą `zip()`**
- Tworzy listę par `(liczba, litera)`, np. `[(23, 'A'), (5, 'X')]`.
- Przydatne do przetwarzania powiązanych danych.

### 🔹 3. **Operacje na danych**
- **Sortowanie listy liczb** – wykorzystuje funkcję `sorted()`.
- **Obliczanie pierwiastków kwadratowych** – `math.sqrt()` oblicza pierwiastki z liczb dodatnich.
- Wyniki są zapisywane w nowych listach.

### 🔹 4. **Obsługa wyjątków**
- `ZeroDivisionError` – obsługa błędu dzielenia przez zero.
- `TypeError` – zabezpieczenie przed błędami związanymi z typami danych.
- Funkcja `safe_division()` zwraca wynik lub komunikat błędu.

### 🔹 5. **Pomiar czasu wykonywania kodu**
- `time.time()` mierzy czas rozpoczęcia i zakończenia operacji.
- Wynik podawany jest w sekundach.

## 🛠 Moduły Pythona
- **Python 3** – [Oficjalna dokumentacja](https://docs.python.org/3/)
- **Moduły standardowe:**
  - `math` – [Dokumentacja](https://docs.python.org/3/library/math.html)
    - [`math.sqrt(x)`](https://docs.python.org/3/library/math.html#math.sqrt) – oblicza pierwiastek kwadratowy z `x`.
  - `random` – [Dokumentacja](https://docs.python.org/3/library/random.html)
    - [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint) – losuje liczbę całkowitą z zakresu `[a, b]`.
    - [`random.sample(population, k)`](https://docs.python.org/3/library/random.html#random.sample) – wybiera `k` unikalnych elementów z listy.
  - `time` – [Dokumentacja](https://docs.python.org/3/library/time.html)
    - [`time.time()`](https://docs.python.org/3/library/time.html#time.time) – zwraca czas w sekundach od epoki UNIX.
- **Wbudowane funkcje Pythona:**
  - [`zip()`](https://docs.python.org/3/library/functions.html#zip) – łączy elementy z kilku list w pary.
  - [`sorted()`](https://docs.python.org/3/library/functions.html#sorted) – zwraca posortowaną listę.
  - [`chr()`](https://docs.python.org/3/library/functions.html#chr) – konwertuje liczbę całkowitą na odpowiadający jej znak Unicode.
  - [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance) – sprawdza, czy obiekt jest instancją określonego typu lub klasy.
- **Obsługa wyjątków:**
  - [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError) – wyjątek przy dzieleniu przez zero.
  - [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError) – wyjątek związany z nieprawidłowym typem danych.

## 🚀 Uruchomienie
1. Pobierz repozytorium:  
   git clone https://github.com/KrzysztofTurko/python-intro.git
2. Przejdź do katalogu:  
   `cd python-intro`  
3. Uruchom program:  
   `python zadanie_1.py`
