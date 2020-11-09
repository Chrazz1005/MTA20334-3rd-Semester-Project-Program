import cv2
import numpy as np
import time


class Thresholding:
    # ------------ Image Definitions ------------



    # ------------ Count Program Execution Time ------------
    startTime = time.time()

    def splitImage(self, image):
        r, g, b = cv2.split(image)

        return r  # Since the image is "binary", being either 0 in all channels or 255, it doesn't matter which channel is returned
    # ------------ Binary Function ------------
    def binarize(self, image):
        outputImage = np.zeros(image.shape, dtype=image.dtype)
        # For every row in the input image we receive the y coordinate and the row
        print('starting binary loop...')
        for y, row in enumerate(image):
            # For every pixel in row we receive the x coordinate and the pixel value
            for x, pixel in enumerate(row):
                # Initializing the color value R, G, B
                H, S, V = pixel[0], pixel[1], pixel[2]
                if H in range(35, 115) and S in range(115, 240) and V in range(0, 200):
                    #H in range(0, 90) and S in range(40, 195) and V in range(20, 170):
                    #H in range(0, 80) and S in range(0, 195) and V in range(25, 170):
                    # If so, turn the pixel white
                    outputImage[y, x] = 255
                else:
                    # If not, turn the pixel black
                    outputImage[y, x] = 0

        print('binary pic is now binary yes')
        outputImage = self.splitImage(outputImage)
        return outputImage


if __name__ == '__main__':
    inputImage = cv2.imread("Pictures/Green_Hand_One_W_Background.png", cv2.COLOR_BGR2HSV)
    thresh = Thresholding()

    binary = thresh.binarize(inputImage)
    cv2.imshow("Hand Spread", inputImage)
    cv2.imshow("Hand Spread Binary", binary)

    print("Program Execution Time: %s" % round(time.time() - thresh.startTime), "seconds")
    cv2.waitKey(0)