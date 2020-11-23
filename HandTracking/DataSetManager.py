import os
from tqdm import tqdm
from AspectRatio import *
from Compactness import *
from GrassFire import *
from Thresholding import *
from database import *


class DataSetManager:
    testDirectory = ""
    savePath = ""
    picturesCount = 0
    allCompactness = []
    allAspectRatio = []
    executionTime = time.time()
    enableGrassFire = True
    calculateCompactness = True
    calculateAspectRatio = True

    def dataLoop(self):
        userInput = input("Image Directory:" + "\n")
        self.testDirectory = userInput
        userInput = input("Save Path:" + "\n")
        self.savePath = userInput
        print("+-------------------------+")
        print("| Image Loop Started.     |")
        print("| Directory:", self.testDirectory, "   |")
        print("| Save Path:", self.savePath, " |")
        print("| ----------------------- |")
        print("| Images in Directory:", len(os.listdir(self.testDirectory)), "|")
        print("+-------------------------+")
        for images in tqdm(os.listdir(self.testDirectory)):
            if images.endswith(".jpg") or images.endswith(".png"):
                nonBinarized = cv2.imread(self.testDirectory + "/" + str(images), cv2.IMREAD_COLOR)
                thresh = Thresholding()
                binarized = thresh.binarize(nonBinarized)
                if self.enableGrassFire:
                    gf = GrassFire(binarized)
                    gf.startGrassFire()

                gc = GeometryCalculator(binarized)
                gc.resetVariables()

                if self.calculateCompactness:
                    c = Compactness(binarized)
                    self.allCompactness.append(c.calculateCompactness())

                if self.calculateAspectRatio:
                    ar = AspectRatio(binarized)
                    ar.calculateArea()
                    self.allAspectRatio.append(ar.calculateAspectRatio())

                # print("Image " + str(images) + " Is Done \n" + "Proceeding... \n")
                self.picturesCount += 1
                cv2.imwrite(os.path.join(self.savePath, "Binarized_" + str(images)), binarized)
            else:
                print("No Image(s) found", "ERROR: Wrong filetype")

    def useDatabase(self):
        db = Database()
        for i in range(0, len(self.allCompactness)):
            db.mdbAdd(i, self.allCompactness[i], self.allAspectRatio[i], self.allCompactness[i], self.allAspectRatio[i],
                      self.allCompactness[i], self.allAspectRatio[i])

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
        print("Min", min(self.allCompactness))
        print("Max", max(self.allCompactness))
        print("+-------- Aspect Ratio --------+")
        print("Elements in Aspect Ratio", self.allAspectRatio)
        print("Avg. Aspect Ratio", self.Average(self.allAspectRatio))
        print("Min", min(self.allAspectRatio))
        print("Max", max(self.allAspectRatio))
        print("+------------------------------+")


# test = DataSetManager()
# test.dataLoop()
# test.useDatabase()
# test.printTestingResults()
