import math
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
        print("| Directory:", self.testDirectory, )
        print("| Save Path:", self.savePath)
        print("+-------------------------+")
        print("| Images in Directory:", len(os.listdir(self.testDirectory)))
        print("+-------------------------+")
        for images in tqdm(os.listdir(self.testDirectory)):
            if images.endswith(".jpg") or images.endswith(".png"):
                nonBinarized = cv2.imread(self.testDirectory + "/" + str(images), cv2.IMREAD_COLOR)

                thresh = Thresholding()
                binarized = thresh.binarize(nonBinarized)

                gr = GrassFire(binarized)
                grassArray = gr.startGrassFire()

                bb = BoundingBox(grassArray)
                croppedImage = bb.cropImage()

                ap = AspectRatio(croppedImage)
                self.aspectRatioResult.append(ap.calculateAspectRatio())

                cp = Compactness(croppedImage)
                self.compactnessResult.append(cp.calculateCompactness())

                ph = ProjectionHistogram(croppedImage)
                self.histogramMaxHeightRelation.append(ph.checkMaxHeightRelation())
                self.histogramHorizontalRatio.append(ph.checkHoriSizeRatio())
                self.histogramVerticalRatio.append(ph.checkVertSizeRatio())
                self.histogramMaxHeightDiffRelation.append(ph.checkMaximumRelations())

                # cv2.imwrite("./DataSetPics/binary%d.jpg" % frameCount, grass)
                ed = EuclideanDistance()
                ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                            ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())

                # print("Image " + str(images) + " Is Done \n" + "Proceeding... \n")
                self.picturesCount += 1
                cv2.imwrite(os.path.join(self.savePath, "Binarized_" + str(images)), croppedImage)
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

    def normalizeData(self):
        data = [self.compactnessResult, self.aspectRatioResult, self.histogramMaxHeightRelation,
                self.histogramHorizontalRatio, self.histogramVerticalRatio, self.histogramMaxHeightDiffRelation]
        data_normalized = data / np.linalg.norm(data)
        return list(data_normalized)

    def stanardDeviance(self):
        zum = []
        sd = []
        for i in range(0, len(self.normalizeData())):
            avg = sum(self.normalizeData()[i]) / len(self.normalizeData()[i])
            for j in range(0, len(self.normalizeData())):
                zum.append(sum(pow(self.normalizeData()[j] - avg, 2)))
            n = len(self.normalizeData()[i])-1
            sd.append(math.sqrt(zum[i] / n))

        return sd

    def printTestingResults(self):
        print("+-------- Test Results --------+")
        print("Images tested:", self.picturesCount)
        print("Execution time: %s" % round((time.time() - self.executionTime), 2), "seconds")
        print("+-------- Compactness ---------+")
        print("Elements in Compactness", self.compactnessResult)
        print("Avg. Compactness", self.Average(self.compactnessResult))
        print("Min", min(self.compactnessResult))
        print("Max", max(self.compactnessResult))
        print("+-------- Aspect Ratio --------+")
        print("Elements in Aspect Ratio", self.aspectRatioResult)
        print("Avg. Aspect Ratio", self.Average(self.aspectRatioResult))
        print("Min", min(self.aspectRatioResult))
        print("Max", max(self.aspectRatioResult))
        print("+-------- Projection Histogram --------+")
        print("Elements in Max Height", self.histogramMaxHeightRelation)
        print("Elements in Horizontal Ratio", self.histogramHorizontalRatio)
        print("Elements in Vertical Ratio", self.histogramVerticalRatio)
        print("Elements in Max Height Diff", self.histogramMaxHeightDiffRelation)
        print("+-------- Data Sets --------+")
        print("Compactness Dataset", self.compactnessResult)
        print("Aspect Ratio Dataset", self.aspectRatioResult)
        print("Histogram Max Height Relation Dataset", self.histogramMaxHeightRelation)
        print("Histogram Hori Dataset", self.histogramHorizontalRatio)
        print("Histogram Vert Dataset", self.histogramVerticalRatio)
        print("Histogram Max Height Diff Dataset", self.histogramMaxHeightDiffRelation)
        print("+-------- Standard Deviance --------+")
        print("C, A, HMHRD, HHD, HVD, HMHDD", self.stanardDeviance())
        for i in range(0, len(self.normalizeData())):
            print("average", self.Average(self.normalizeData()[i]))
        print("+------------------------------+")


test = DataSetManager()
test.dataLoop()
test.printTestingResults()
