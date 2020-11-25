import os
from tqdm import tqdm
from HandTracking.AspectRatio import *
from HandTracking.Compactness import *
from HandTracking.EuclideanDistance import *
from HandTracking.GrassFire import *
from HandTracking.ProjectionHistograms import *
from HandTracking.Thresholding import *
from HandTracking.Database import *
from HandTracking.BoundingBox import *


class DataSetManager:
    testDirectory = ""
    savePath = ""
    picturesCount = 0
    compactnessResult = []
    aspectRatioResult = []
    histogramMaxHeightRelation = []
    histogramHorizontalRatio = []
    histogramVerticalRatio = []
    histogramMaxHeightDiffRelation = []
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
        print("| Image Loop Started.")
        print("| Directory:", self.testDirectory,)
        print("| Save Path:", self.savePath)
        print("+-------------------------+")
        print("| Images in Directory:", len(os.listdir(self.testDirectory)), "|")
        print("+-------------------------+")
        for images in tqdm(os.listdir(self.testDirectory)):
            if images.endswith(".jpg") or images.endswith(".png"):
                nonBinarized = cv2.imread(self.testDirectory + "/" + str(images), cv2.IMREAD_COLOR)

                print("Starting Threshold...")
                thresh = Thresholding()
                binarized = thresh.binarize(nonBinarized)
                print("Threshold finished.")

                print("Starting GrassFire...")
                gr = GrassFire(binarized)
                grassArray = gr.startGrassFire()
                print("GrassFire finished.")

                print("Starting BoundingBox...")
                bb = BoundingBox(grassArray)
                croppedImage = bb.cropImage()
                print("BoundingBox finished.")

                print("Starting AspectRatio...")
                ap = AspectRatio(croppedImage)
                self.aspectRatioResult.append(ap.calculateAspectRatio())
                print("AspectRatio finished.")

                print("Starting Compactness...")
                cp = Compactness(croppedImage)
                self.compactnessResult.append(cp.calculateCompactness())
                print("Compactness finished.")

                print("Starting ProjectionHistogram...")
                ph = ProjectionHistogram(croppedImage)
                self.histogramMaxHeightRelation.append(ph.checkMaxHeightRelation())
                self.histogramHorizontalRatio.append(ph.checkHoriSizeRatio())
                self.histogramVerticalRatio.append(ph.checkVertSizeRatio())
                self.histogramMaxHeightDiffRelation.append(ph.checkMaximumRelations())
                print("ProjectionHistogram finished.")

                print("Starting EuclideanDistance...")
                # cv2.imwrite("./DataSetPics/binary%d.jpg" % frameCount, grass)
                ed = EuclideanDistance()
                ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                            ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())
                print("EuclideanDistance finished.")

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


test = DataSetManager()
test.dataLoop()
test.printTestingResults()
