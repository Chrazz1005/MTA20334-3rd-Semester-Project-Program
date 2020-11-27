import numpy as np
import cv2


class ColorFinder:

    def __init__(self, image):
        self.image = image

    def findAverageColor(self):
        convertedImage = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        npArray = np.array(np.asarray(convertedImage))
        for y, row in enumerate(npArray):
            for x, pixel in enumerate(row):
                H, S, V = pixel[2], pixel[1], pixel[0]
                if H in range(40, 70) and S in range(0, 255) and V in range(0, 255):
                    npArray[y, x] = H, S, V
                    print("FOUND")
                else:
                    npArray[y, x] = 0, 0, 0
                    print("NOPE")
        return npArray


image = cv2.imread("PicsEval/A1.jpg")
cf = ColorFinder(image)
converted = cf.findAverageColor()
cv2.imshow("Converted", converted)
cv2.waitKey(0)
print(converted)
