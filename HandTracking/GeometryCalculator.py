import cv2
import numpy as np


class GeometryCalculator:
    whitePixelCoords = []
    wMaxY, wMaxX = 0, 0
    wMinY, wMinX = 0, 0
    allWhitePixels, allBlackPixels = 0, 0
    whitePixelsY, whitePixelsX = [], []
    blackPixelsY, blackPixelsX = [], []

    def cPoints(self, image):
        binaryImageHeight = image.shape[0]
        binaryImageWidth = image.shape[1]

        for y in range(0, binaryImageHeight):
            for x in range(0, binaryImageWidth):
                if image[y, x] == 255:
                    self.allWhitePixels += 1
                    self.whitePixelsY.append(y)
                    self.whitePixelsX.append(x)
                else:
                    self.allBlackPixels += 1
                    self.blackPixelsY.append(y)
                    self.blackPixelsX.append(x)

        self.wMaxY, self.wMinY = max(self.whitePixelsY), min(self.whitePixelsY)
        self.wMaxX, self.wMinX = max(self.whitePixelsX), min(self.whitePixelsX)

        for i in range(0, len(self.whitePixelsY)):
            self.whitePixelCoords.append([self.whitePixelsY[i], self.whitePixelsX[i]])

        cv2.rectangle(image, (self.wMaxX, self.wMaxY), (self.wMinX, self.wMinY), color=255, thickness=1)
