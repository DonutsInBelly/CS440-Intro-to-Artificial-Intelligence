#!/usr/bin/python3

import network
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

nn = network.NeuralNetwork()
colors = np.genfromtxt('color.csv', delimiter=',')
input_data = np.genfromtxt('input.csv', delimiter=',')

picture = np.genfromtxt('data.csv', delimiter=',')

nn.inputarr(input_data, colors)

np.savetxt("output.csv", nn.colorizeGiven(picture,input_data), delimiter=",")
