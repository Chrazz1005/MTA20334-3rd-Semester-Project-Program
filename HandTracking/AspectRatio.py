from BoundingBox import *


class AspectRatio:
    handGesture = ""

    def __init__(self, image):
        self.image = image

    def calculateAspectRatio(self):
        height = self.image.shape[0]
        width = self.image.shape[1]

        if width != 0:
            aspectRatio = (height / width)
            return aspectRatio
        else:
            return "width = 0"

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

