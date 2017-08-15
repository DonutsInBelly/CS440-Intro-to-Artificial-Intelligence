import numpy as np

# sigmoid function
def sigmoid(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1.0/(1+np.exp(-x))

def blockshaped(arr, nrows, ncols):
    """
    Return an array of shape (n, nrows, ncols) where
    n * nrows * ncols = arr.size

    If arr is a 2D array, the returned array should look like n subblocks with
    each subblock preserving the "physical" layout of arr.
    """
    h, w = arr.shape
    return (arr.reshape(h//nrows, nrows, -1, ncols)
               .swapaxes(1,2)
               .reshape(-1, nrows, ncols))

def unblockshaped(arr, h, w):
    """
    Return an array of shape (h, w) where
    h * w = arr.size

    If arr is of shape (n, nrows, ncols), n sublocks of shape (nrows, ncols),
    then the returned array preserves the "physical" layout of the sublocks.
    """
    n, nrows, ncols = arr.shape
    return (arr.reshape(h//nrows, -1, nrows, ncols)
               .swapaxes(1,2)
               .reshape(h, w))

class NeuralNetwork(object):
    """docstring for NeuralNetwork."""
    def __init__(self):
        super(NeuralNetwork, self).__init__()

    # Should return grayscale image and build a model to use
    def train(self, rgb):
        self.rgb = rgb
        self.height = len(rgb)
        self.width = len(rgb[0])
        # create a numpy array to hold grayscale image
        gray = np.ndarray((len(rgb),len(rgb[0])))
        # for each pixel in rgb, calculate grayscale version of it and add it to gray numpy array
        for x in range(len(rgb)):
            for y in range(len(rgb[x])):
                gray[(x,y)] = int((rgb[(x,y,0)] * 0.21) + (rgb[(x,y,1)] * 0.72) + (rgb[(x,y,2)] * 0.07))
                print('Pixel: ' + str(x) + ',' + str(y) + ' with value: ' + str(gray[(x,y)]))
        self.gray = gray

        # Build vectors to make linear combinations easier
        self.patch = blockshaped(self.gray, 3, 3)
        self.gray9 = np.empty([len(self.patch), 10])
        for i in range(len(self.patch)):
            tmp = self.patch[i]
            tmp = tmp.flatten()
            tmp = np.append(tmp, 1)
            self.gray9[i] = tmp
        # print(self.gray9)

        # Build array of corresponding center rgb values
        self.center = np.empty([len(self.patch), 3])
        index = 0
        rgbarr = np.array(rgb)
        for row in range(1, self.height, 3):
            for col in range(1, self.width, 3):
                self.center[index] = rgbarr[(row,col)]
                index += 1
                print("Checking pixel ("+str(row)+","+str(col)+")")

        # Initialize random weight vectors
        self.alpha = 0.001
        self.weightsR = np.random.random_sample((len(self.patch), 10))
        self.weightsG = np.random.random_sample((len(self.patch), 10))
        self.weightsB = np.random.random_sample((len(self.patch), 10))
        # print(self.weightsG)

        # Train weight sets
        for updates in range(1):
            print("Training set: "+str(updates))
            # Pick a patch and corresponding center value
            for row in range(len(self.gray9)):
                real = self.center[row]
                inputR = np.sum(np.multiply(self.weightsR[row],self.gray9[row]))
                inputG = np.sum(np.multiply(self.weightsG[row],self.gray9[row]))
                inputB = np.sum(np.multiply(self.weightsB[row],self.gray9[row]))
                outputR = sigmoid(inputR)
                outputG = sigmoid(inputG)
                outputB = sigmoid(inputB)
                # print(outputR)
                # Update weights
                for col in range(len(self.gray9[row])):
                    self.weightsR[(row,col)] = self.weightsR[(row,col)] - self.alpha*(2*(outputR - real[0])*sigmoid(inputR,deriv=True)*self.gray9[(row,col)])
                    self.weightsG[(row,col)] = self.weightsG[(row,col)] - self.alpha*(2*(outputG - real[1])*sigmoid(inputG,deriv=True)*self.gray9[(row,col)])
                    self.weightsB[(row,col)] = self.weightsB[(row,col)] - self.alpha*(2*(outputB - real[2])*sigmoid(inputB,deriv=True)*self.gray9[(row,col)])
        print(self.weightsR)
        return gray

    def colorize(self, img):
        gray = np.ndarray((len(img),len(img[0])))
        for row in range(len(img)):
            for col in range(len(img[row])):
                gray[(row,col)] = img[(row,col,0)]
                # print(img[(row,col,0)])

        # Build vectors to compare
        patch = blockshaped(gray, 3, 3)
        vectors = np.empty([len(patch),10])
        for i in range(len(patch)):
            tmp = patch[i]
            tmp = tmp.flatten()
            tmp = np.append(tmp, 1)
            vectors[i] = tmp

        # Build color image
        diff = 1
        vallist = []
        for index in range(len(vectors)):
            for index2 in range(len(self.gray9)):
                if np.allclose(vectors[index], self.gray9[index2], rtol=diff):
                    # Found a good match
                    R = np.sum(np.multiply(vectors[index], self.weightsR))
                    G = np.sum(np.multiply(vectors[index], self.weightsG))
                    B = np.sum(np.multiply(vectors[index], self.weightsB))
                    # value = np.array([R,G,B])
                    value = self.center[index2]
                    # print(value)
                    vallist.append(value)
                    break

        count = 0
        for row in range(1, len(img), 3):
            for col in range(1, len(img[row]), 3):
                img[(row,col)] = vallist[count]

                img[(row+1,col+1)] = vallist[count]
                img[(row+1,col)] = vallist[count]
                img[(row+1,col-1)] = vallist[count]
                img[(row,col-1)] = vallist[count]
                img[(row,col+1)] = vallist[count]
                img[(row-1,col-1)] = vallist[count]
                img[(row-1,col)] = vallist[count]
                img[(row-1,col+1)] = vallist[count]

                count += 1

        return img
