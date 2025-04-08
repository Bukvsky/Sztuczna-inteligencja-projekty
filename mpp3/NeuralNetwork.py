from Perceptron import Perceptron
import math
import os
from FileReader import fileReader
class NeuralNetwork:
    def __init__(self,input_size,num_of_languages,learning_rate,threshold):
        self.perceptrons = []
        self.frequency = generateListOfLanguages() #znormalizowana częstotliwość
        self.learning_rate = learning_rate
        for label in self.frequency:
            self.perceptrons.append(Perceptron(label,input_size,threshold,learning_rate))

    def train(self, max_epochs=1000, error_threshold=0.01):
        print("🚀 Rozpoczynam trening (tryb: identycznościowy, targety ±1)")
        print(f"🔢 Liczba języków: {len(self.perceptrons)}")
        print("=" * 50)

        epoch = 0
        converged = False
        error_history = []

        while not converged and epoch < max_epochs:
            epoch += 1
            total_error = 0
            correct_predictions = 0
            total_samples = 0

            for lang, vector in self.frequency.items():
                # Normalizacja wektora wejściowego
                input_norm = math.sqrt(sum(x ** 2 for x in vector))
                normalized_input = [x / input_norm for x in vector] if input_norm > 0 else vector

                # Obliczamy wyjścia wszystkich perceptronów
                outputs = []
                for perceptron in self.perceptrons:
                    net = sum(w * x for w, x in zip(perceptron.weights[:-1], normalized_input)) + perceptron.weights[-1]
                    outputs.append(net)

                # Określamy, który perceptron powinien "wygrać"
                correct_index = next(i for i, p in enumerate(self.perceptrons) if p.label == lang)
                predicted_index = outputs.index(max(outputs))

                if predicted_index == correct_index:
                    correct_predictions += 1
                total_samples += 1

                # Uczenie: aktualizujemy wagi KAŻDEGO perceptrona
                for i, perceptron in enumerate(self.perceptrons):
                    target = 1.0 if i == correct_index else -1.0
                    output = outputs[i]
                    error = target - output
                    total_error += error ** 2

                    lr = self.learning_rate * (1.0 / (1.0 + 0.001 * epoch))  # malejący learning rate

                    # Aktualizacja wag
                    for j in range(len(normalized_input)):
                        perceptron.weights[j] += lr * error * normalized_input[j]
                    perceptron.weights[-1] += lr * error  # bias

                    # Normalizacja wag
                    norm = math.sqrt(sum(w ** 2 for w in perceptron.weights))
                    if norm > 0:
                        perceptron.weights = [w / norm for w in perceptron.weights]

            avg_error = total_error / (len(self.perceptrons) * len(self.frequency))
            accuracy = correct_predictions / total_samples
            error_history.append(avg_error)

            if accuracy == 1.0:
                converged = True
                print(f"\n🎉 Sukces! Wszystkie próbki poprawnie sklasyfikowane w epoce {epoch}")
            elif len(error_history) > 20 and abs(avg_error - sum(error_history[-20:]) / 20) < 1e-5:
                print(f"\n⚠️ Trening zatrzymany - brak poprawy przez 20 epok (błąd utknął na ~{avg_error:.6f})")
                break

            if epoch % 25 == 0 or epoch == 1 or converged:
                print(f"⏳ Epoka {epoch:>4}: błąd = {avg_error:.6f}, dokładność = {accuracy:.2%}")

        print("\n📉 Historia błędów (ostatnie 20 epok):")
        for e, err in enumerate(error_history[-20:], start=max(1, len(error_history) - 19)):
            print(f"Epoka {e:>4}: {'▇' * int(err * 50)} {err:.6f}")

        return avg_error



    def test(self, test_data):
        print("\n🧪 Rozpoczynam testowanie na danych testowych...")
        total = 0
        correct = 0
        for lang, vector in test_data.items():


                total += 1

                # Normalizacja wektora wejściowego
                input_norm = math.sqrt(sum(x ** 2 for x in vector))
                normalized_input = [x / input_norm for x in vector] if input_norm > 0 else vector

                # Obliczamy odpowiedzi wszystkich perceptronów (y = net)
                outputs = []
                for perceptron in self.perceptrons:
                    net = sum(w * x for w, x in zip(perceptron.weights[:-1], normalized_input)) + perceptron.weights[-1]
                    outputs.append(net)

                predicted_index = outputs.index(max(outputs))
                predicted_label = self.perceptrons[predicted_index].label

                if predicted_label == lang:
                    correct += 1

                print(
                    f"📄 Próbka: {lang:<12} ➡️ Przewidziano: {predicted_label:<12} {'✅' if predicted_label == lang else '❌'}")

        accuracy = correct / total if total > 0 else 0
        print("\n📊 Podsumowanie testów:")
        print(f"✔️ Poprawnych: {correct}")
        print(f"❌ Błędnych:    {total - correct}")
        print(f"🎯 Dokładność: {accuracy:.2%}")

        return accuracy

    def classify(self, vector):

        if vector is None:
            return "❌ Nie można określić języka - tekst nie zawiera wystarczającej liczby liter"

        # Klasyfikacja
        results = []
        for perceptron in self.perceptrons:
            net = sum(w * x for w, x in zip(perceptron.weights[:-1], vector)) + perceptron.weights[-1]
            results.append((perceptron.label, net))

        # Sortowanie wyników
        results.sort(key=lambda x: x[1], reverse=True)
        best_lang, best_score = results[0]

        # Generowanie przyjaznego wyniku
        output = []
        output.append("\n🌈 WYNIK KLASYFIKACJI")
        output.append("=" * 40)
        output.append("\n🏆 Najbardziej prawdopodobny język:")
        output.append(f"✨ {best_lang.upper()} (pewność: {self._score_to_percent(best_score):.1f}%)")

        output.append("\n🔍 Pełna lista wyników:")
        for lang, score in results[:5]:  # Tylko top 5 wyników
            output.append(
                f"• {lang.upper():<12} {self._score_to_percent(score):5.1f}% {'🌟' if lang == best_lang else ''}")

        return "\n".join(output)

    def _score_to_percent(self, score):
        """Konwertuje wynik na procenty w zakresie 0-100%"""
        return min(max(0, (score + 1) * 50), 100)

def normalizeVector(vector):
    norm = round(math.sqrt(sum(x**2 for x in vector)),4)
    normalized_vector = [round(x/norm,6) for x in vector]
    return normalized_vector


def generateListOfLanguages():
    countries = {}
    for filename in os.listdir('.\\dane\\language_texts_grouped\\'):
        fr = fileReader('.\\dane\\language_texts_grouped\\'+filename+'\\')
        fr.generatePercentDict()
        sortedDict = dict(sorted(fr.charsPercentDict.items()))
        t = []
        for item  in sortedDict:
            t.append(sortedDict[item])
        countries[filename] = normalizeVector(t)
    return countries
