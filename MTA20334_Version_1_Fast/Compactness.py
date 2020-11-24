class Compactness:
    debug = True
    allPixelsInBoundary = 0

    def __init__(self, image):
        self.image = image

    def calculateCompactness(self):
        height = self.image.shape[0]
        width = self.image.shape[1]
        # Calculating the area by multiplying the height with the width
        area = (height * width)

        allWhitePixels = len(self.image[self.image == 255])
        # Compactness is calculated by taking 100 and dividing it with the area multiplied with all the white pixels
        compactness = round((100 / area) * allWhitePixels)
        return compactness

    def compactnessComparison(self):
        if self.calculateCompactness() in range(80, 85):
            handGesture = "A"
        elif self.calculateCompactness() in range(75, 85):
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
