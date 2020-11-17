import cv2
import numpy as np
import time


class Thresholding:
    startTime = time.time()

    # x, y = (image > limit).nonzero()
    # vals = image[x, y]

    def convertToHSV(self, image):
        for x, row in enumerate(image):
            for y, col in enumerate(row):
                red = col[2] / 255
                green = col[1] / 255
                blue = col[0] / 255
                maximum = max(red, green, blue)
                minimum = min(red, green, blue)
                delta = maximum - minimum

                hue = 0
                if delta == 0:
                    pass
                elif maximum == red:
                    hue = (60 * (((green - blue) / delta) % 6)) % 360
                elif maximum == green:
                    hue = (60 * ((blue - red) / delta + 2)) % 360
                elif maximum == blue:
                    hue = (60 * ((red - green) / delta + 4)) % 360

                value = maximum * 255

                if maximum == 0:
                    saturation = 0
                else:
                    saturation = delta / maximum * 255

                image[x, y] = [hue / 2, round(saturation), round(value)]

        return image

    def binarize(self, image):
        imageConverted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        npArray = np.array(np.asarray(imageConverted))

        Range = [(30, 80), (0, 255), (0, 255)]
        redColorRange = np.logical_and(Range[0][0] < npArray[:, :, 0], npArray[:, :, 0] < Range[0][1])
        greenColorRange = np.logical_and(Range[1][0] < npArray[:, :, 1], npArray[:, :, 1] < Range[1][1])
        blueColorRange = np.logical_and(Range[2][0] < npArray[:, :, 2], npArray[:, :, 2] < Range[2][1])
        rgbRange = (redColorRange * greenColorRange * blueColorRange)

        npArray[rgbRange] = 255
        npArray[np.logical_not(rgbRange)] = 0

        r, g, b = cv2.split(npArray)
        return r

    #print("Program Execution Time: %s" % (time.time() - startTime), "seconds")

if __name__ == '__main__':
    TH = Thresholding()
    img = cv2.imread('./PicsEval/A1.jpg')
    bImg = TH.binarize(img)

    print(bImg)
    cv2.imshow('b', bImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()