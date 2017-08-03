#!/usr/bin/python3
# import numpy as np
# import scipy.misc as sp
#
# print(sp.__dict__.keys())
# # im = scipy.misc.imread("image1.jpg")
# # print(im)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('image1.jpg')
gray = rgb2gray(img)
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.show()
