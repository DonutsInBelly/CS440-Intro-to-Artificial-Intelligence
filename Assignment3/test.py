#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

colors = np.genfromtxt('color.csv', delimiter=',')
input_data = np.genfromtxt('input.csv', delimiter=',')

picture = np.genfromtxt('data.csv', delimiter=',')
print(picture)

# picture.flatten()
# for i in range(len(picture)):

plt.imshow(picture)
plt.show()
