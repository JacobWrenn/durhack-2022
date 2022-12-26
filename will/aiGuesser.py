import numpy as np
import random
import math

input_vector1 = np.array([17, 5])
input_vector2 = np.array([1, 6])
# Modified from Durham CT 9.2 Neural Network Example

class NeuralNetwork:
    def __init__(self, learning_rate):
        
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def _compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2

        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)

        derror_dbias = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dbias
        )
        derror_dweights = (
            derror_dprediction * dprediction_dlayer1 * dlayer1_dweights
        )

        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (
            derror_dweights * self.learning_rate
        )

learning_rate = 0.1

def neuralRandom(realValue=21):
    neural_network = NeuralNetwork(learning_rate)

    if neural_network.predict(input_vector1) < 0.5:
        return realValue-(3*(neural_network.predict(input_vector2)))
    else:
        return realValue+(3*(neural_network.predict(input_vector2)))

def neuralRandomType(type, realValue=None):
    if type == 'temp':
        if realValue == None:
            realValue = 21
        mult = 1.5
    if type == 'hum':
        if realValue == None:
            realValue = 44
        mult = 3.5
    if type == 'co2':
        if realValue == None:
            realValue == 200
        mult = 100

    neural_network = NeuralNetwork(learning_rate)

    if neural_network.predict(input_vector1) < 0.5:
        return realValue-(mult*(neural_network.predict(input_vector2)))
    else:
        return realValue+(mult*(neural_network.predict(input_vector2)))

# USE NEURAL RANDOM FUNCTION
