import random


class Perceptron:

    def __init__(self,l, weights, threshold, learning_rate ):
        if weights is None:
            self.weights = [random.uniform(-0.1, 0.1) for _ in range(l + 1)]
        else:
            self.weights = weights

        if learning_rate is None:
            self.learning_rate = 1
        else:
            self.learning_rate = learning_rate

        self.threshold = threshold

    #Obliczanie wyjścia perceptronu
    def compute(self, inputs):
        # print(self.weights, inputs)
        # print("Inputy",inputs)
        suma = sum(self.weights[i] * inputs[i] for i in range(len(inputs)))+self.weights[-1]
        #print(f'''Suma: {suma}, dla progu: {self.threshold}, wynik:{1 if suma >= self.threshold else 0}''')
        return 1 if suma >= self.threshold else 0
    #Uczenie Perceptronu
    def learn(self,input,target):
        out = self.compute(input)
        error = target - out
        for i in range(len(input)):
            self.weights[i] += self.learning_rate * error * input[i]
        """if error != 0:
            self.threshold = self.threshold - self.learning_rate*error"""

        self.weights[-1] += self.learning_rate * error




