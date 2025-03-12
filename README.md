🎯 Narzędzia Pomocnicze w Pythonie

📌 Opis
"Narzędzia Pomocnicze w Pythonie" to zestaw praktycznych funkcji ułatwiających pracę z danymi w języku Python. Projekt został stworzony w sposób modułowy, co umożliwia łatwe rozszerzanie i modyfikowanie kodu.

Kluczowe możliwości obejmują generowanie losowych danych, operacje matematyczne, sortowanie, obsługę błędów oraz mierzenie czasu wykonywania programów. Może on posłużyć jako fundament do dalszej eksploracji i rozwijania kompetencji programistycznych.

⚙️ Funkcjonalności

🔢 1. Tworzenie losowych danych

Generowanie listy losowych liczb całkowitych z przedziału 0–100.

Tworzenie listy losowych liter od A do Z.

Każde uruchomienie programu zwraca nowe wartości.

🔗 2. Łączenie list za pomocą zip()

Tworzenie listy par (np. [(12, 'G'), (45, 'M')]), co umożliwia łączenie powiązanych informacji.

Przydatne do pracy z danymi o wspólnych indeksach.

📊 3. Operacje na danych

Sortowanie list liczbowych przy użyciu funkcji sorted().

Obliczanie pierwiastków kwadratowych z liczb dodatnich przy pomocy math.sqrt().

Wyniki operacji są przechowywane w osobnych strukturach danych.

🛡️ 4. Obsługa błędów

Obsługa błędu dzielenia przez zero (ZeroDivisionError).

Zapobieganie błędom związanym z nieprawidłowymi typami danych (TypeError).

Funkcja safe_division() zwraca wynik obliczeń lub odpowiedni komunikat w przypadku błędu.

⏳ 5. Pomiar czasu wykonania

Wykorzystanie time.time() do pomiaru czasu rozpoczęcia i zakończenia operacji.

Wynik zwracany jest w sekundach, co umożliwia analizę wydajności.

📚 Moduły Pythona

W projekcie korzystano z Pythona 3 oraz standardowych modułów:

Python 3 – https://docs.python.org/3/

Moduły standardowe:

math – https://docs.python.org/3/library/math.html

math.sqrt(x) – https://docs.python.org/3/library/math.html#math.sqrt – oblicza pierwiastek kwadratowy z x.

random – https://docs.python.org/3/library/random.html

random.randint(a, b) – https://docs.python.org/3/library/random.html#random.randint – losuje liczbę całkowitą z zakresu [a, b].

random.sample(population, k) – https://docs.python.org/3/library/random.html#random.sample – wybiera k unikalnych elementów z listy.

time – https://docs.python.org/3/library/time.html

time.time() – https://docs.python.org/3/library/time.html#time.time – zwraca czas w sekundach od epoki UNIX.

Wbudowane funkcje Pythona:

zip() – https://docs.python.org/3/library/functions.html#zip – łączy elementy z kilku list w pary.

sorted() – https://docs.python.org/3/library/functions.html#sorted – zwraca posortowaną listę.

chr() – https://docs.python.org/3/library/functions.html#chr – konwertuje liczbę całkowitą na odpowiadający jej znak Unicode.

isinstance() – https://docs.python.org/3/library/functions.html#isinstance – sprawdza, czy obiekt jest instancją określonego typu lub klasy.

Obsługa wyjątków:

ZeroDivisionError – https://docs.python.org/3/library/exceptions.html#ZeroDivisionError – wyjątek przy dzieleniu przez zero.

TypeError – https://docs.python.org/3/library/exceptions.html#TypeError – wyjątek związany z nieprawidłowym typem danych.

🚀 Jak uruchomić projekt?

Pobierz repozytorium:

git clone https://github.com/KrzysztofTurko/python-intro.git

Przejdź do katalogu projektu:

cd python-intro

Uruchom główny plik programu:

python zadanie_1.py

