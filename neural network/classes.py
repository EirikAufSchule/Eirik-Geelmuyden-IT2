import numpy as np

def cost(result, ideal):




class Neuron():

    def __init__(self, bias, value):
        self.bias = bias
        self.value = value

    def activation(self, weig, a):
        product_sum = 0
        for i, j in w, a:
            product_sum += i*j
        self.value = self.sigmoid(product_sum + self.bias)

    def sigmoid(x):
        return 1/(1 + np.exp(-x)) 