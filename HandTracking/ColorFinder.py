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


image = cv2.imread("B_ONLY_HAND/B7.png")

# A1: 75, 48, 77
# A2: 86, 49, 75
# A3: 91, 38, 74
# A4: 90, 46, 76
# A5: 91, 39, 60
# A6: 76, 26, 67
# A7: 105, 35, 69
# A8: 85, 33, 72
# A9: 74, 34, 64
# A10: 76, 29, 58
# A11: 68, 43, 63

# B1: 75, 49, 78
# B2: 106, 32, 76
# B3: 88, 34, 73
# B4: 88, 43, 78
# B5: 92, 33, 67
# B6: 74, 23, 74
# B7: 104, 31, 77
# B8:
# B9:
# B10:
# B11:


cf = ColorFinder(image)
converted = cf.findAverageColor()
cv2.imshow("Average Color", converted)
cv2.waitKey(0)
print(converted)
