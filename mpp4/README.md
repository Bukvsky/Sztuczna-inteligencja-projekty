# MPP 4 – Klasyfikator Naiwny Bayesowski dla zbioru danych Iris

## Opis projektu

Projekt realizuje klasyfikator Naiwnego Bayesa od podstaw, bez użycia bibliotek machine learningowych, do klasyfikacji danych z klasycznego zbioru **Iris**.

## Dane wejściowe

- `iris_training.txt` – zbiór danych treningowych  
- `iris_test.txt` – zbiór danych testowych

Każdy rekord zawiera cztery cechy (liczby zmiennoprzecinkowe) oraz etykietę klasy.

## Funkcjonalności

- Nauka modelu na podstawie danych treningowych:
  - Zliczanie częstości dla danych dyskretnych
  - Obliczanie średnich i odchyleń standardowych dla danych ciągłych
- Obsługa dwóch trybów klasyfikacji:
  - **Dyskretny** – z wygładzaniem Laplace’a
  - **Ciągły (Gaussian Naive Bayes)** – z wygładzaniem pierwszego atrybutu, jeśli odchylenie standardowe wynosi 0
- Wyświetlanie:
  - Dokładności klasyfikacji (accuracy) w procentach
  - Macierzy omyłek (confusion matrix)
  - Prawdopodobieństw przed i po wygładzaniu (dla pierwszego atrybutu)
- **Tryb ręczny** – użytkownik może wpisywać wektory cech i uzyskać klasyfikację

## Wymagania

- Python 3.x
- Brak bibliotek zewnętrznych – implementacja w czystym Pythonie (`math` to jedyna biblioteka)


