import cv2
import numpy as np
import math
import time
from GeometryCalculator import *


class Compactness:
    binaryImage = cv2.imread("framePicture.png", 0)
    debug = True
    allPixelsInBoundary = 0
    # allWhitePixels, allBlackPixels = 0, 0
    # wMaxY, wMaxX = 0, 0
    # wMinY, wMinX = 0, 0
    # whitePixelsY, whitePixelsX = [], []
    # blackPixelsY, blackPixelsX = [], []
    # whitePixelCoords = []

    # def findCornerPoints(self, image):
    #     binaryImageHeight = image.shape[0]
    #     binaryImageWidth = image.shape[1]
    #
    #     for y in range(0, binaryImageHeight):
    #         for x in range(0, binaryImageWidth):
    #             if image[y, x] == 255:
    #                 self.allWhitePixels += 1
    #                 self.whitePixelsY.append(y)
    #                 self.whitePixelsX.append(x)
    #             else:
    #                 self.allBlackPixels += 1
    #                 self.blackPixelsY.append(y)
    #                 self.blackPixelsX.append(x)
    #
    #     self.wMaxY, self.wMinY = max(self.whitePixelsY), min(self.whitePixelsY)
    #     self.wMaxX, self.wMinX = max(self.whitePixelsX), min(self.whitePixelsX)
    #
    #     for i in range(0, len(self.whitePixelsY)):
    #         self.whitePixelCoords.append([self.whitePixelsY[i], self.whitePixelsX[i]])
    #
    #     cv2.rectangle(image, (self.wMaxX, self.wMaxY), (self.wMinX, self.wMinY), color=255, thickness=1)
    gc = GeometryCalculator()
    gc.cPoints(binaryImage)

    def calculateCompactness(self):
        areal = ((self.gc.wMaxY + 1 - self.gc.wMinY) * (self.gc.wMaxX + 1 - self.gc.wMinX))
        compactness = round((100 / areal) * self.gc.allWhitePixels)
        return compactness

    def compactnessComparison(self):
        if self.calculateCompactness() in range(55, 100):
            handGesture = "A"
        elif self.calculateCompactness() in range(15, 45):
            handGesture = "C"
        else:
            handGesture = "Not Found"

        return handGesture

    def printResults(self):
        print("+---------------- PRINT DETAILS ----------------+")
        print("| MAX X:", self.gc.wMaxX, "MAX Y:", self.gc.wMaxY)
        print("| MIN X:", self.gc.wMinX, "MIN Y:", self.gc.wMinY)
        print("|------------------------------------------------")
        print("| Total White Pixels:", self.gc.allWhitePixels)
        print("| Total Black Pixels:", self.gc.allBlackPixels)
        print("| Total Pixels:", (self.gc.allWhitePixels + self.gc.allBlackPixels))
        print("|------------------------------------------------")
        print("| The white pixels fills:", self.calculateCompactness(), "%")
        print("|------------------------------------------------")
        print("| Hand Gesture Detected as:", self.compactnessComparison())
        print("+-----------------------------------------------+")
