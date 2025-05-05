# Jednowarstwowa Sieć Neuronowa do Klasyfikacji Języków

## 📌 Opis projektu

Program implementuje jednowarstwową sieć neuronową (złożoną z perceptronów) do klasyfikacji tekstów w różnych językach na podstawie częstotliwości występowania liter w tekście.

## 🎯 Cel projektu

Celem projektu jest rozpoznawanie języka tekstu na podstawie:
- Proporcji występowania poszczególnych liter alfabetu łacińskiego
- Użyciu jednowarstwowej sieci neuronowej z K perceptronami (gdzie K to liczba rozpoznawanych języków)

## 📂 Struktura danych

Program wymaga przygotowania dwóch katalogów:
1. `./dane/language_texts_grouped/` - zawierającego podkatalogi z tekstami treningowymi
2. `./test/` - zawierającego teksty testowe

Każdy podkatalog w katalogu treningowym powinien być nazwany nazwą języka i zawierać co najmniej 10 tekstów (min. 2 akapity każdy).

## 🧠 Algorytm

1. **Przetwarzanie tekstu**:
   - Usuwanie znaków specjalnych i diakrytyków
   - Zliczanie częstotliwości występowania liter a-z
   - Normalizacja wektorów cech

2. **Sieć neuronowa**:
   - Jeden perceptron na każdy język
   - Funkcja aktywacji: identycznościowa (y = net)
   - Uczenie z momentum i adaptacyjnym współczynnikiem uczenia
   - Normalizacja wag po każdej iteracji

3. **Klasyfikacja**:
   - Wybór języka z najwyższą wartością wyjściową perceptronu
   - Obliczanie pewności klasyfikacji w procentach

## 🚀 Funkcjonalności

1. **Trening modelu**:
   - Automatyczne wykrywanie języków z folderu danych
   - Monitorowanie postępów treningu (błąd, dokładność)
   - Wczesne zatrzymanie przy braku poprawy

2. **Testowanie**:
   - Automatyczne testowanie na przygotowanych danych testowych
   - Wyświetlanie dokładności klasyfikacji

3. **Interaktywna klasyfikacja**:
   - Możliwość wprowadzenia własnego tekstu
   - Wyświetlanie top 5 najbardziej prawdopodobnych języków
   - Wizualizacja pewności klasyfikacji

## 🛠️ Użycie

1. Uruchom program: `python main.py`
2. Wybierz opcję:
   - `1` - Trenuj i testuj model
   - `2` - Klasyfikuj własny tekst
   - `3` - Wyjście

## 📊 Przykładowe wyniki

```
🌈 WYNIK KLASYFIKACJI
========================================

🏆 Najbardziej prawdopodobny język:
✨ POLISH (pewność: 92.5%)

🔍 Pełna lista wyników:
• POLISH       92.5% 🌟
• CZECH        85.2% 
• SLOVAK       78.9% 
• ENGLISH      65.4% 
• GERMAN       59.1% 
```

## 📌 Wymagania

- Python 3.x
- Biblioteka `unidecode` (do usuwania diakrytyków)

## 📝 Uwagi

- Wszystkie elementy sieci neuronowej zaimplementowane od podstaw
- Brak użycia zewnętrznych bibliotek ML
- Pełna kontrola nad procesem uczenia i klasyfikacji
