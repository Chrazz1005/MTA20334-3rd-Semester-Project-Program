import cv2


class GeometryCalculator:
    debug = False
    whitePixelCoords = []
    wMaxY, wMaxX = 0, 0
    wMinY, wMinX = 0, 0
    allWhitePixels, allBlackPixels = 0, 0
    whitePixelsY, whitePixelsX = [], []
    blackPixelsY, blackPixelsX = [], []

    def __init__(self, image):
        self.image = image

    def cPoints(self):
        binaryImageHeight = self.image.shape[0]
        binaryImageWidth = self.image.shape[1]

        for y in range(0, binaryImageHeight):
            for x in range(0, binaryImageWidth):
                if self.image[y, x] == 255:
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

        cv2.rectangle(self.image, (self.wMaxX, self.wMaxY), (self.wMinX, self.wMinY), color=255, thickness=1)

    def resetEveryFuckingThing(self):
        self.whitePixelCoords.clear()
        self.wMaxY, self.wMaxX = 0, 0
        self.wMinY, self.wMinX = 0, 0
        self.allWhitePixels, self.allBlackPixels = 0, 0
        self.whitePixelsY.clear()
        self.whitePixelsX.clear()
        self.blackPixelsY.clear()
        self.blackPixelsX.clear()

    def cPointsPrintResult(self):
        print("+---------------- PRINT DETAILS ----------------+")
        print("| MAX X:", self.wMaxX, "MAX Y:", self.wMaxY)
        print("| MIN X:", self.wMinX, "MIN Y:", self.wMinY)
        print("|------------------------------------------------")
        print("| Total White Pixels:", self.allWhitePixels)
        print("| Total Black Pixels:", self.allBlackPixels)
        print("| Total Pixels:", (self.allWhitePixels + self.allBlackPixels))
        print("|------------------------------------------------")

    def startGeometryCalculations(self):
        self.cPoints()
        if self.debug:
            self.cPointsPrintResult()
