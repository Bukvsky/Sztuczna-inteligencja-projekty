# K-Means – Klasteryzacja zbioru Iris

## Opis projektu

Ten projekt implementuje algorytm **k-średnich (k-means)** w języku Python, bez użycia bibliotek zewnętrznych. Na koniec obliczana jest **entropia** każdego klastra oraz ogólna **entropia na podstawie zadanych częstości**. Przeznaczone dla danych z klasycznego zbioru **Iris**.

## Funkcje główne

- Losowe inicjalizowanie centroidów
- Przypisywanie punktów do najbliższego centroidu (klastra)
- Aktualizacja centroidów
- Obliczanie **SSE** (sumy kwadratów odległości punktów od centroidu)
- Automatyczne zatrzymanie po osiągnięciu stabilizacji SSE
- Obliczanie **entropii każdego klastra**
- Obliczanie **entropii z zadanych częstości** (zadanie dodatkowe)
- Obsługa błędów (np. brak pliku wejściowego)

## Struktura danych

- Plik `iris_test.txt` powinien zawierać dane w formacie:
- 5.1 3.5 1.4 0.2 Iris-setosa
  
