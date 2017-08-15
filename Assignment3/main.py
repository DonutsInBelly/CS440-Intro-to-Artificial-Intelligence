#!/usr/bin/python3

import network
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

nn = network.NeuralNetwork()
img = mpimg.imread('profile.jpg')
newgray = mpimg.imread('image123.jpg')
# print(img[0])

gray = nn.train(img)

# plt.imshow(gray, cmap='gray')
# plt.show()

newimg = nn.colorize(newgray)

plt.imshow(newimg)
plt.show()
