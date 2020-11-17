from GeometryCalculator import *

from HandTracking.GeometryCalculator import GeometryCalculator


class Compactness:
    debug = False
    allPixelsInBoundary = 0

    def __init__(self, image):
        self.image = image

    def calculateCompactness(self):
        gc = GeometryCalculator(self.image)
        gc.cPoints()
        area = ((gc.wMaxY + 1 - gc.wMinY) * (gc.wMaxX + 1 - gc.wMinX))
        compactness = round((100 / area) * gc.allWhitePixels)
        return compactness

    # 77,85
    def compactnessComparison(self):
        if self.calculateCompactness() in range(75, 85):
            handGesture = "A"
        elif self.calculateCompactness() in range(80, 85):
            handGesture = "B"
        elif self.calculateCompactness() in range(45, 50):
            handGesture = "C"
        else:
            handGesture = "Not Found"

        return handGesture

    def printResults(self):
        print("| Compactness:", self.calculateCompactness(), "%")
        print("|------------------------------------------------")
        print("| Hand Gesture Detected as:", self.compactnessComparison())
        print("+-----------------------------------------------+")

