import cv2


class BoundingBox:
    debug = False
    allWhitePixels, allBlackPixels = 0, 0
    height = 0
    width = 0

    def __init__(self, image):
        self.image = image

    def cropImage(self):
        # Define height and width from the constructor's image input.
        binaryImageHeight = self.image.shape[0]
        binaryImageWidth = self.image.shape[1]

        wMaxY, wMaxX = 0, 0
        wMinY, wMinX = binaryImageHeight, binaryImageWidth

        # Loop through the image with y, x as the unpacked values.
        for y in range(0, binaryImageHeight):
            for x in range(0, binaryImageWidth):
                # Every time the image iterates over a white pixel.
                if self.image[y, x] == 255:
                    # Count the amount of white pixels.
                    self.allWhitePixels += 1
                    # Define maximum and minimum values
                    if wMinX > x:
                        wMinX = x
                    if wMaxX < x:
                        wMaxX = x
                    if wMinY > y:
                        wMinY = y
                    if wMaxY < y:
                        wMaxY = y

        self.height = (wMaxY - wMinY) + 1
        self.width = (wMaxX - wMinX) + 1

        crop_img = self.image[wMinY:wMinY + self.height, wMinX:wMinX + self.width]

        print(self.height, self.width)

        if self.debug:
            cv2.rectangle(self.image, (wMaxX, wMaxY), (wMinX, wMinY), color=150, thickness=1)
            cv2.imshow("img rect", self.image)
            cv2.waitKey(0)
            cv2.imshow("img", crop_img)
            cv2.waitKey(0)

        return crop_img

    def cPointsPrintResult(self):
        print("+---------------- PRINT DETAILS ----------------+")
        print("| MAX X:", self.wMaxX, "MAX Y:", self.wMaxY)
        print("| MIN X:", self.wMinX, "MIN Y:", self.wMinY)
        print("|------------------------------------------------")

    def startGeometryCalculations(self):
        self.cropImage()
        if self.debug:
            self.cPointsPrintResult()
