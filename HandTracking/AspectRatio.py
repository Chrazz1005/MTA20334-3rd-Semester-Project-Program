import cv2
import numpy as np
from GeometryCalculator import *


class AspectRatio:
    Billede = cv2.imread("Binarized_Pictures/B2.png", 0)
    handGesture = ""

    gc = GeometryCalculator()
    gc.cPoints(Billede)

    def calculateAreal(self):
        height = (self.gc.wMaxY - self.gc.wMinY) + 1
        width = (self.gc.wMaxX - self.gc.wMinX) + 1
        areal = (height * width)
        return areal, height, width

    def calculateAspectRatio(self):
        aspectRatio = (self.calculateAreal()[1] / self.calculateAreal()[2])
        return aspectRatio

    def compareAspectRatio(self):
        handGesture = ""
        if 2.1 < self.calculateAspectRatio() < 2.5 or 2.5 < self.calculateAspectRatio() < 2.1:
            handGesture = "A"
        elif 1.7 < self.calculateAspectRatio() < 2.0 or 2.0 < self.calculateAspectRatio() < 1.7:
            handGesture = "B"
        elif 0.6 < self.calculateAspectRatio() < 1.3 or 1.3 < self.calculateAspectRatio() < 0.6:
            handGesture = "C"
        else:
            print("No Hand Gesture Detected.")

        return handGesture
