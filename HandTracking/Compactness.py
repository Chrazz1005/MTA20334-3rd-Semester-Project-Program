from GeometryCalculator import *


class Compactness:
    binaryImage = cv2.imread("Binarized_Pictures/hres.png", 0)
    debug = True
    allPixelsInBoundary = 0

    def __init__(self, image):
        self.image = image

    def calculateCompactness(self):
        gc = GeometryCalculator(self.image)
        gc.cPoints()
        area = ((gc.wMaxY + 1 - gc.wMinY) * (gc.wMaxX + 1 - gc.wMinX))
        compactness = round((100 / area) * gc.allWhitePixels)
        return compactness

    def compactnessComparison(self):
        if self.calculateCompactness() in range(55, 100):
            handGesture = "A"
        elif self.calculateCompactness() in range(15, 50):
            handGesture = "C"
        else:
            handGesture = "Not Found"

        return handGesture

    def printResults(self):
        print("| Compactness:", self.calculateCompactness(), "%")
        print("|------------------------------------------------")
        print("| Hand Gesture Detected as:", self.compactnessComparison())
        print("+-----------------------------------------------+")

