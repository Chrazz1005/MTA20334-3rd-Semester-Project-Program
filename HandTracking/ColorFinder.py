import numpy as np
import cv2


class ColorFinder:

    def __init__(self, image):
        self.image = image

    def findAverageColor(self):
        convertedImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        npArray = np.array(np.asarray(convertedImage))
        npArray[:, :, 0], npArray[:, :, 1], npArray[:, :, 2] = np.average(npArray, axis=(0, 1))
        return npArray


image = cv2.imread("PicsEval/A1.jpg")
cf = ColorFinder(image)
converted = cf.findAverageColor()
cv2.imshow("Converted", converted)
cv2.waitKey(0)
print(converted)
