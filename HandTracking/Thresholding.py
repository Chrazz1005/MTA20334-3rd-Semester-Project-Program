import cv2
import numpy as np
import time


class Thresholding:
    # ------------ Image Definitions ------------
    inputImage = cv2.imread("Pictures/Green_Hand_One_W_Background.png", cv2.COLOR_BGR2HSV)
    outputImage = np.zeros(inputImage.shape, dtype=inputImage.dtype)

    # ------------ Count Program Execution Time ------------
    startTime = time.time()

    # ------------ Binary Function ------------
    def binarize(self, image):
        # For every row in the input image we receive the y coordinate and the row
        for y, row in enumerate(image):
            # For every pixel in row we receive the x coordinate and the pixel value
            for x, pixel in enumerate(row):
                # Initializing the color value R, G, B
                H, S, V = pixel[0], pixel[1], pixel[2]
                if H in range(0, 80) and S in range(0, 195) and V in range(25, 170):
                    # If so, turn the pixel white
                    self.outputImage[y, x] = 255
                else:
                    # If not, turn the pixel black
                    self.outputImage[y, x] = 0


thresh = Thresholding()

thresh.binarize(thresh.inputImage)
cv2.imshow("Hand Spread", thresh.inputImage)
cv2.imshow("Hand Spread Binary", thresh.outputImage)

print("Program Execution Time: %s" % round(time.time() - thresh.startTime), "seconds")
cv2.waitKey(0)