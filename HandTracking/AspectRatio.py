from GeometryCalculator import *


class AspectRatio:
    handGesture = ""
    height = 0
    width = 0
    areal = 0

    def __init__(self, image):
        self.image = image

    def calculateArea(self):
        gc = GeometryCalculator(self.image)
        gc.cPoints()
        self.height = (gc.wMaxY - gc.wMinY) + 1
        self.width = (gc.wMaxX - gc.wMinX) + 1
        self.areal = (self.height * self.width)

    def calculateAspectRatio(self):
        aspectRatio = (self.height / self.width)
        return round(aspectRatio, 2)

    def compareAspectRatio(self):
        handGesture = ""
        if 1.7 < self.calculateAspectRatio() < 2.0 or 2.0 < self.calculateAspectRatio() < 1.7:
            handGesture = "Gesture_A"
        elif 2.1 < self.calculateAspectRatio() < 2.5 or 2.5 < self.calculateAspectRatio() < 2.1:
            handGesture = "Gesture_B"
        elif 0.6 < self.calculateAspectRatio() < 1.3 or 1.3 < self.calculateAspectRatio() < 0.6:
            handGesture = "Gesture_C"
        else:
            print("No Hand Gesture Detected.")

        return handGesture

