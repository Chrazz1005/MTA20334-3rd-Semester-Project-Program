import os
from tqdm import tqdm
from AspectRatio import *
from Compactness import *
from GrassFire import *
from Thresholding import *


class DataSetManager:
    testDirectory = "A"
    savePath = "Binarized"
    picturesCount = 0
    allCompactness = []
    allAspectRatio = []
    executionTime = time.time()
    enableGrassFire = False
    calculateCompactness = False
    calculateAspectRatio = False

    def dataLoop(self):
        print("-----------------------")
        print("Image Loop Started.")
        print("Directory:", self.testDirectory)
        print("Save Path:", self.savePath)
        print("-----------------------")
        for images in tqdm(os.listdir(self.testDirectory)):
            if images.endswith(".jpg") or images.endswith(".png"):
                nonBinarized = cv2.imread("NonBinarized/" + str(images), cv2.IMREAD_COLOR)
                thresh = Thresholding()
                binarized = thresh.binarize(nonBinarized)
                binarizedGray = cv2.cvtColor(binarized, cv2.COLOR_BGR2GRAY)

                if self.enableGrassFire:
                    gf = GrassFire(binarizedGray)
                    gf.startGrassFire()

                gc = GeometryCalculator(binarizedGray)
                gc.resetEveryFuckingThing()

                if self.calculateCompactness:
                    c = Compactness(binarizedGray)
                    c.calculateCompactness()
                if self.calculateAspectRatio:
                    ar = AspectRatio(binarizedGray)

                self.picturesCount += 1
                cv2.imwrite(os.path.join(self.savePath, "Binarized_" + str(images)), binarized)

                if self.calculateCompactness:
                    self.allCompactness.append(c.calculateCompactness())

                if self.calculateAspectRatio:
                    self.allAspectRatio.append(ar.calculateAspectRatio())

                # print("Image " + str(images) + " Is Done \n" + "Proceeding... \n")
                time.sleep(0.1)
            else:
                print("No Image(s) found", "ERROR: Wrong filetype")

    def Average(self, length):
        avg = sum(length) / len(length)
        return avg

    def printTestingResults(self):
        print("+-------- Test Results --------+")
        print("Images tested:", self.picturesCount)
        print("Execution time: %s" % round((time.time() - self.executionTime), 2), "seconds")
        print("+-------- Compactness ---------+")
        print("Elements in Compactness", self.allCompactness)
        print("Avg. Compactness", self.Average(self.allCompactness))
        print("+-------- Aspect Ratio --------+")
        print("Elements in Aspect Ratio", self.allAspectRatio)
        print("Avg. Aspect Ratio", self.Average(self.allAspectRatio))
        print("+------------------------------+")


test = DataSetManager()
test.dataLoop()
test.printTestingResults()
