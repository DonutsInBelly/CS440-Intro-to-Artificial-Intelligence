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
    gray = np.ndarray((len(rgb),len(rgb[0])))
    for x in range(len(rgb)):
        for y in range(len(rgb[x])):
            gray[(x,y)] = int((rgb[(x,y,0)] * 0.21) + (rgb[(x,y,1)] * 0.72) + (rgb[(x,y,2)] * 0.07))
            print(gray[(x,y)])
    return gray


img = mpimg.imread('profile.jpg')
gray = rgb2gray(img)
model = {}
newColor = 0
seenColor = 0

print(newColor)
print(seenColor)
plt.gray()
plt.imshow(gray)
plt.show()
