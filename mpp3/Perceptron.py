import math
import random


class Perceptron:

    def __init__(self,input_size,threshold,learning_rate ):
        self.weights = [random.uniform(-0.1, 0.1) for _ in range(input_size + 1)]
        self.learning_rate = learning_rate
        self.threshold = threshold

    #Normalize vector
    def normalize(self,vector):
        norm = math.sqrt((sum([x**2 for x in vector])))
        return [x/norm for x in vector]


    #Calculate scalar product
    def dot_product(self,inputs):
        return sum([self.weights[i] * inputs[i] for i in range(len(inputs))]) + self.weights[-1]

    #activation function
    def compute(self,inputs):
        inputs = self.normalize(inputs)
        return self.dot_product(inputs)

    def learn(self,inputs,target):
        inputs = self.normalize(inputs)
        net = self.compute(inputs)
        error = target-net
        for i in range(len(inputs)):
            self.weights[i]+=self.learning_rate*error*inputs[i]

        self.weights = self.normalize(self.weights)
        self.weights[-1] += self.learning_rate*error

