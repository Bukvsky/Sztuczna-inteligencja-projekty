import math
from unidecode import unidecode
from FileReader import fileReader
from NeuralNetwork import NeuralNetwork
import os
import string


def makeDictionary(text):
    tmp = {letter: 0 for letter in string.ascii_lowercase}
    total_letters = sum(c.isalpha() for c in text)

    if total_letters == 0:  # Avoid division by zero
        return tmp

    for char in text:
        if char in tmp:
            tmp[char] += 1

    # Normalize by total letter count
    for letter in tmp:
        tmp[letter] = tmp[letter] / total_letters

    return tmp

def loadTestData():
    languages_test = {}
    for filename in os.listdir(".\\test"):
        try:
            with open(f".\\test\\{filename}", 'r', encoding='utf-8') as file:
                text = file.read()

            text = unidecode(text.lower())
            allowed_chars = set(string.ascii_lowercase + ' \n')
            cleaned_text = ''.join(c for c in text if c in allowed_chars)

            # Store with filename as key
            tmp = makeDictionary(cleaned_text)
            languages_test[filename[:-4]] = [tmp[x] for x in tmp]
        except Exception as e:
            print(f"Error processing file {filename}: {str(e)}")
            continue

    return languages_test


def text_to_vector(text):

    text = unidecode(text.lower())

    allowed_chars = set(string.ascii_lowercase + ' \n')
    cleaned_text = ''.join(c for c in text if c in allowed_chars)

    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    total_letters = 0

    for char in cleaned_text:
        if char in string.ascii_lowercase:
            letter_counts[char] += 1
            total_letters += 1

    if total_letters == 0:
        return None

    vector = [letter_counts[letter] / total_letters
              for letter in sorted(letter_counts.keys())]

    norm = math.sqrt(sum(x ** 2 for x in vector))
    if norm > 0:
        normalized_vector = [x / norm for x in vector]
    else:
        normalized_vector = vector

    return normalized_vector


def main():
    # Wczytanie danych
    test_data = loadTestData()
    num_languages = len(os.listdir(".\\dane\\language_texts_grouped"))

    # Inicjalizacja sieci neuronowej
    neural_network = NeuralNetwork(26, num_languages, 0.01, 0.5)

    print("=" * 50)
    print("🛠️ SYSTEM KLASYFIKACJI JĘZYKÓW 🛠️")
    print("=" * 50)

    while True:
        print("\n1. 🏋️ Trenuj i testuj model")
        print("2. 🔍 Klasyfikuj własny tekst")
        print("3. 🚪 Wyjście")
        choice = input("\nWybierz opcję (1-3): ")

        if choice == "1":
            print("\n" + "=" * 50)
            print("🏋️ TRENOWANIE MODELU")
            print("=" * 50)
            epochs_needed = neural_network.train(10000)
            print(f"\n✅ Trening zakończony po {epochs_needed} epokach")

            print("\n" + "=" * 50)
            print("🧪 TESTOWANIE MODELU")
            print("=" * 50)
            neural_network.test(test_data)

        elif choice == "2":
            print("\n" + "=" * 50)
            print("🔍 KLASYFIKACJA TEKSTU")
            print("=" * 50)
            text = input("Wprowadź tekst do analizy: ")

            # Przetwarzanie tekstu na wektor cech
            try:
                vector = text_to_vector(text)
                print(vector)
                if vector is None:
                    print("❌ Błąd: Nie udało się przetworzyć tekstu")
                    continue

                # Klasyfikacja
                result = neural_network.classify(vector)
                print(f"\n🔎 Wynik: Tekst jest w języku {result['language'].upper()}")
                print(f"💯 Pewność: {result['confidence']:.2%}")

            except Exception as e:
                print(f"❌ Błąd podczas przetwarzania: {str(e)}")

        elif choice == "3":
            print("\n" + "=" * 50)
            print("👋 ZAKOŃCZONO PRACĘ PROGRAMU")
            print("=" * 50)
            break

        else:
            print("❌ Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")



if __name__ == '__main__':
    main()
