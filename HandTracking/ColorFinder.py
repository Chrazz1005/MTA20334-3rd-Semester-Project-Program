import numpy as np
import cv2
from HandTracking.Thresholding import *


class ColorFinder:

    def __init__(self, image):
        self.image = image

    def findAverageColor(self):
        npArray = np.array(np.asarray(self.image))
        npArray[:, :, 0], npArray[:, :, 1], npArray[:, :, 2] = np.average(npArray, axis=(0, 1))
        # convertedImage = cv2.cvtColor(npArray, cv2.COLOR_BGR2HSV)
        return npArray

    def Average(self, length):
        avg = sum(length) / len(length)
        return avg


image = cv2.imread("C_ONLY_HAND/C11.png")

cf = ColorFinder(image)
converted = cf.findAverageColor()
print(cf.Average(list))
