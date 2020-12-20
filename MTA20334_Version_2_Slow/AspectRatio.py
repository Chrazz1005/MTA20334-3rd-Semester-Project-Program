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

