import math
import random


class Perceptron:
    def __init__(self, label, input_size, threshold, learning_rate):
        self.label = label
        # Inicjalizacja wag z mniejszym zakresem (-0.05 do 0.05)
        self.weights = [random.uniform(-0.05, 0.05) for _ in range(input_size + 1)]  # +1 dla biasu
        self.initial_learning_rate = learning_rate
        self.learning_rate = learning_rate
        self.threshold = threshold
        self.best_weights = None
        self.best_error = float('inf')
        self.momentum = [0] * (input_size + 1)  # Do momentum

    def normalize(self, vector):
        """Normalizacja wektora do długości 1"""
        norm = math.sqrt(sum(x ** 2 for x in vector))
        if norm > 0:
            return [x / norm for x in vector]
        return vector

    def net(self, inputs):
        """Iloczyn skalarny z uwzględnieniem biasu"""
        return sum(w * x for w, x in zip(self.weights[:-1], inputs)) + self.weights[-1]

    def activate(self, x):
        """Funkcja aktywacji tanh - ogranicza wyjście do [-1, 1]"""
        return math.tanh(x)

    def update_weights(self, inputs, target):
        """Aktualizacja wag z momentum i adaptacyjnym learning rate"""
        output = self.activate(self.dot_product(inputs))
        error = target - output

        # Oblicz aktualizacje wag
        updates = [self.learning_rate * error * x for x in inputs]

        # Zastosuj momentum (0.9 to typowa wartość)
        updates_with_momentum = [update + 0.9 * prev
                                 for update, prev in zip(updates, self.prev_updates[:-1])]

        # Aktualizuj wagi (bez biasu)
        for i in range(len(inputs)):
            self.weights[i] += updates_with_momentum[i]

        # Aktualizuj bias (ostatni element)
        self.weights[-1] += self.learning_rate * error

        # Zapamiętaj aktualizacje dla następnego kroku
        self.prev_updates = updates + [self.learning_rate * error]

        return error ** 2  # Zwróć błąd kwadratowy

    def decay_learning_rate(self, epoch):
        """Zmniejsz learning rate w czasie"""
        self.learning_rate = self.initial_learning_rate * (0.99 ** epoch)

    def conditional_normalize(self):
        """Normalizuj wagi tylko jeśli ich norma przekracza 1.0"""
        norm = math.sqrt(sum(w ** 2 for w in self.weights))
        if norm > 1.0:
            self.weights = [w / norm for w in self.weights]

    def save_best_weights(self, current_error):
        """Zapisz najlepsze wagi jeśli błąd się poprawił"""
        if current_error < self.best_error:
            self.best_error = current_error
            self.best_weights = self.weights.copy()