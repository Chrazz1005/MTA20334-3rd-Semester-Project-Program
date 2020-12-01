import os
import cv2


class AverageColorLoop:
    def __init__(self, image):
        self.image = image

    def averageColorLoop(self):
        img = self.image
        documentName = "array"
        hueArray = []
        saturationArray = []
        valueArray = []

        convertedImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        fileHue = open("Arrays/hueArray.txt", "w")
        fileSat = open("Arrays/satArray.txt", "w")
        fileVal = open("Arrays/valArray.txt", "w")
        for y, row in enumerate(convertedImage):
            for x, value in enumerate(row):
                # with open(os.path.join("Arrays", documentName), "w") as file:
                Hue, Saturation, Value = value[0], value[1], value[2]
                CRAZY_RED_COLOR = (255, 0, 0)

                if Hue != CRAZY_RED_COLOR[0] and Saturation != CRAZY_RED_COLOR[1] and Value != CRAZY_RED_COLOR[2]:
                    hueArray.append(Hue)
                    saturationArray.append(Saturation)
                    valueArray.append(Value)

        fileHue.write(str(hueArray))
        fileSat.write(str(saturationArray))
        fileVal.write(str(valueArray))
        fileHue.close()
        fileSat.close()
        fileVal.close()



image = cv2.imread("A_Only_Hand/A1.png")
acl = AverageColorLoop(image)
acl.averageColorLoop()
