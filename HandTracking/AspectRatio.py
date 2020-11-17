from GeometryCalculator import *


class AspectRatio:
    handGesture = ""

    def __init__(self, image):
        self.image = image

    def calculateArea(self):
        gc = GeometryCalculator(self.image)
        gc.cPoints()
        height = (gc.wMaxY - gc.wMinY) + 1
        width = (gc.wMaxX - gc.wMinX) + 1
        areal = (height * width)
        return areal, height, width

    def calculateAspectRatio(self):
        aspectRatio = (self.calculateArea()[1] / self.calculateArea()[2])
        return round(aspectRatio, 2)

    def compareAspectRatio(self):
        handGesture = ""
        if 1.7 < self.calculateAspectRatio() < 2.0 or 2.0 < self.calculateAspectRatio() < 1.7:
            handGesture = "A"
        elif 2.1 < self.calculateAspectRatio() < 2.5 or 2.5 < self.calculateAspectRatio() < 2.1:
            handGesture = "B"
        elif 0.6 < self.calculateAspectRatio() < 1.3 or 1.3 < self.calculateAspectRatio() < 0.6:
            handGesture = "C"
        else:
            print("No Hand Gesture Detected.")

        return handGesture

