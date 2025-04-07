# MPP 2 - Perceptron Delta Learning Algorithm

## Opis zadania
Ten projekt implementuje perceptron uczący się metodą delty w celu klasyfikacji irysów. Model ma za zadanie rozróżnić klasę **Iris-setosa** od dwóch pozostałych klas na podstawie zbioru danych.

## Dane wejściowe
- **Dane treningowe** – plik `iris_training.txt`
- **Dane testowe** – plik `iris_test.txt`

Zakładamy, że:
- Atrybut decyzyjny znajduje się w **ostatniej kolumnie**.
- Wszystkie atrybuty poza decyzyjnym są **numeryczne**.
- Liczba atrybutów warunkowych może być dowolna – program nie zakłada stałej liczby cech wejściowych.

## Wymagania
- Implementacja perceptronu **od zera**, bez użycia bibliotek ML.
- Obliczenia wyjścia perceptronu mają być wykonywane wyłącznie za pomocą **operacji arytmetycznych**.
- Implementacja powinna umożliwiać **testowanie perceptronu** na zbiorze testowym oraz **ręczne wprowadzanie danych**.

## Wymagania funkcjonalne
1. **Trening perceptronu** metodą delty na danych treningowych.
2. **Testowanie perceptronu** na danych testowych – program powinien wypisać:
   - Liczbę prawidłowo zaklasyfikowanych przykładów.
   - Dokładność eksperymentu (w procentach).
3. **Interaktywna klasyfikacja** – użytkownik może ręcznie wpisać wektor atrybutów i otrzymać wynik klasyfikacji.

## Implementacja
### Klasa `Perceptron`
Należy zaimplementować klasę `Perceptron`, zawierającą:
- **Pola:**
  - `weights` (wektor wag)
  - `threshold` (próg decyzyjny)
- **Metody:**
  - `Perceptron()` – konstruktor inicjalizujący perceptron.
  - `Compute(inputs)` – obliczanie wyjścia perceptronu dla podanych danych wejściowych.
  - `Learn(inputs, decision)` – nauka perceptronu metodą delty.

### Wczytywanie danych i nauka perceptronu
1. Wczytać z klawiatury **dwie wagi** i **próg perceptronu**.
2. Wczytać **dwa sygnały wejściowe** i ich poprawną odpowiedź.
3. Przeprowadzić proces **nauki perceptronu**.
4. Wydrukować:
   - Końcowe wartości wag.
   - Liczbę wykonanych kroków nauczania.



