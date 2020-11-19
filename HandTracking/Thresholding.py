import cv2
import numpy as np
import time


class Thresholding:
    startTime = time.time()
    testImage = cv2.imread("Gesture_A/A10.jpg", cv2.IMREAD_COLOR)

    # x, y = (image > limit).nonzero()
    # vals = image[x, y]

    def splitImage(self, image):
        r, g, b = cv2.split(image)
        return r

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
        # Converts image to HSV color space (Manual conversion above).
        imageConverted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        # Converts the inputted image to a nparray.
        npArray = np.array(np.asarray(imageConverted))

        # Defines a range for what color to threshold.
        Range = [(30, 80), (0, 255), (0, 255)]

        # Three conditional statements that use the np.logical_and to check for two conditions.
        # if the color channel from nparray is within the above range it returns boolean.
        # It does this for the hue, saturation and value
        # This returns either True or False dependant on if it meets the condition.
        hueColorRange = np.logical_and(Range[0][0] < npArray[:, :, 0], npArray[:, :, 0] < Range[0][1])
        saturationColorRange = np.logical_and(Range[1][0] < npArray[:, :, 1], npArray[:, :, 1] < Range[1][1])
        valueColorRange = np.logical_and(Range[2][0] < npArray[:, :, 2], npArray[:, :, 2] < Range[2][1])

        # hsvRange is the array with only True or False values (True are the white pixels of the hand / False is the
        # black pixels)
        hsvRange = (hueColorRange * saturationColorRange * valueColorRange)

        # Converts the entire array to exist of only 255 values
        npArray[hsvRange] = 255

        # All places in the hsvRange array where the value is false is changed to 0
        npArray[np.logical_not(hsvRange)] = 0

        # Split the channels and return one of the values to return a binary image
        h, s, v = cv2.split(npArray)
        return h
