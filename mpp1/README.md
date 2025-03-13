# MPP 1

**Termin oddania**: 1 tydzień

## Opis zadania

Program powinien wykonać klasyfikację za pomocą algorytmu k-NN (k-Nearest Neighbors) na podstawie danych z plików tekstowych.

### Dane wejściowe:
- **Dane treningowe** – plik `iris_training.txt`
- **Dane testowe** – plik `iris_test.txt`

### Założenia:
- Atrybut decyzyjny znajduje się w ostatniej kolumnie pliku.
- Wszystkie atrybuty, poza decyzyjnym, są numeryczne.
- Program musi obsługiwać dowolną liczbę atrybutów warunkowych (nie zakładając z góry ich liczby).

### Wymagania:
1. Program musi wczytać dane z podanego pliku tekstowego.
2. Program musi zaakceptować wartość parametru `k` (liczba najbliższych sąsiadów) podaną przez użytkownika.
3. Program ma za zadanie zaklasyfikować przykłady wczytane z pliku testowego przy użyciu algorytmu k-NN.
4. Na końcu program wypisuje:
   - Liczbę prawidłowo zaklasyfikowanych przykładów.
   - Dokładność eksperymentu wyrażoną w procentach.

5. Program musi umożliwiać wielokrotne ręczne wpisanie wektora atrybutów i zwrócić wynik klasyfikacji k-NN dla tego wektora.

### Opcjonalnie:
- Dodanie wykresu (np. w Excelu) zależności uzyskanej dokładności od wartości `k`.
- Krótką dyskusję na temat wyników.

### Ważne:
- Program nie może używać żadnych zewnętrznych bibliotek ML.
- Wszystko ma być zaimplementowane ręcznie, np. obliczanie odległości za pomocą działań arytmetycznych.

## Zadania do wykonania:

1. **Wczytanie danych**:
   - Wczytaj dane ze zbioru treningowego (`iris_training.txt`).
   - Wczytaj dane ze zbioru testowego (`iris_test.txt`).

2. **Obliczanie odległości euklidesowych**:
   - Dla pierwszej obserwacji ze zbioru testowego oblicz jej odległości euklidesowe do wszystkich obserwacji w zbiorze treningowym.

3. **Znajdowanie najmniejszych odległości**:
   - Ze znalezionych odległości euklidesowych, wybierz 3 najmniejsze.
   - Wydrukuj wartości decyzyjne dla obserwacji, których te najmniejsze odległości dotyczą.

4. **Wczytanie wektorów i obliczenie odległości**:
   - Wczytaj z klawiatury dwa 4-wymiarowe wektory.
   - Wydrukuj odległość euklidesową/miejską między tymi wektorami.


