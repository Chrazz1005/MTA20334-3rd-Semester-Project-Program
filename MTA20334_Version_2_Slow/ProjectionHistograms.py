import numpy as np
import matplotlib.pyplot as plt
import cv2


class ProjectionHistogram:
    __localDebug = False

    def __init__(self, img):
        self.img = img

    # def splitImage(self):
    #     r, g, b = cv2.split(self.img)
    #     return r  # Since the image is "binary", being either 0 in all channels or 255, it doesn't matter which channel is returned

    def getHistogram_VProjection(self):  ### Gets a vertical projection of the white pixel distribution
        (hY, wY) = self.img.shape[:2]
        sumColsY = []

        # Creates a list containing the sum of the pixels in each column
        for j in range(hY):
            colY = self.img[j:j + 1,
                   0:wY]  # since python is (y, x), the y increments 1 each iteration, whereas the the entire x-row is included to calculate the sum of it.

            sumColsY.append(np.sum(colY))

        if self.__localDebug:
            print('Vertical distribution:', sumColsY)
            print('length vertical array:', len(sumColsY))

        x_axis = []
        for i in range(0, self.img.shape[0]):
            x_axis.append(i)

        # plt.xlabel('Pixel No. (ranging from 0 to the length of y-axis of the image)')
        # plt.ylabel('Sum of white pixels in row y')
        # plt.title('Vertical distribution', fontsize=15)
        # plt.plot(x_axis, sumColsY)
        # plt.show()

        return sumColsY

    def getHistogram_HProjection(self):  ### Gets a horizontal projection of the white pixel distribution
        (hX, wX) = self.img.shape[:2]
        sumColsX = []

        for j in range(wX):
            colX = self.img[0:hX, j:j + 1]  # Same as the vertical projection, but with the axis flipped.

            sumColsX.append(np.sum(colX))
        if self.__localDebug:
            print('Horizontal distribution:', sumColsX)
            print('length horizontal array:', len(sumColsX))
        x_axis = []
        for a in range(0, self.img.shape[1]):
            x_axis.append(a)

        # plt.xlabel('Pixel No. (ranging from 0 to the length of x-axis of the image)')
        # plt.ylabel('Sum of white pixels in col x')
        # plt.title('Horizontal distribution', fontsize=15)
        # plt.plot(x_axis, sumColsX)
        # plt.show()

        return sumColsX

    def trimZeros(self, list):  ##### Removing zeros from (empty space) from the data set
        trimmedList = []
        for i in range(0, len(list)):
            if list[i] != 0:
                trimmedList.append(list[i])

        return trimmedList

    def checkMaxHeightRelation(self):
        horiProject = self.getHistogram_HProjection()
        vertiProject = self.getHistogram_VProjection()

        maxHori = max(horiProject)
        maxVert = max(vertiProject)
        maxHeightRelation = maxVert / maxHori

        ### C range: 1.1 - 1.4
        ### A range: 0.6 - 0.8
        ### B range: 0.35 - 0.6

        return maxHeightRelation

    def checkHoriSizeRatio(self):
        horiProject = self.getHistogram_HProjection()
        lenHori = len(horiProject)
        maxHori = max(horiProject) * 255
        sizeRatioHori = maxHori / lenHori

        if self.__localDebug:
            print('sizeRatioHori', sizeRatioHori)
        return sizeRatioHori

    #### Range for C (testet på 2 billeder); Horizontal: 120 - 200, Vertical: 240-260
    #### Range for A (testet på 3 billeder); Horizontal: 280 - 310, Vertical: 130-160
    #### Range for B (testet på 7 billeder); Horizontal: 320 - 480, Vertical: 100 - 130

    def checkVertSizeRatio(self):
        vertiProject = self.getHistogram_VProjection()
        lenVert = len(vertiProject)
        maxVert = max(vertiProject) * 255
        sizeRatioVert = maxVert / lenVert

        if self.__localDebug:
            print('sizeRatioVert', sizeRatioVert)
        return sizeRatioVert

    def checkMaximumRelations(self):
        vertiProject = self.getHistogram_VProjection()
        localMaximum = 0
        globalMaximum = 0

        for i in range(0, int(len(vertiProject) * 0.30)):
            # print('Første 30%:', vertiProjectvert[i])
            if vertiProject[i] == max(vertiProject[0:int(len(vertiProject) * 0.30)]):
                # print('Første 30% toppunktplacement:', vertiProject.index(vertiProject[i]))
                # print('Første 30% toppunkt valye:', vertiProject[i])
                localMaximum = [vertiProject.index(vertiProject[i]), vertiProject[i]]

        for i in range(int(len(vertiProject) * 0.30), len(vertiProject)):

            if vertiProject[i] == max(vertiProject[int(len(vertiProject) * 0.30):len(vertiProject)]):
                # print('Sidste 70 % toppunktplacement:', vertiProject.index(vertiProject[i]))
                # print('Sidste 70 % toppunkt value:', vertiProject[i])

                globalMaximum = [vertiProject.index(vertiProject[i]), vertiProject[i]]

        if localMaximum and globalMaximum != 0:
            heightDiffRelation = globalMaximum[1] / localMaximum[1]
        else:
            heightDiffRelation = 9999999
            print("No Hand")

        ### C range: 1.8 - 2.2
        ### A range: 0.8 - 1.1
        ### B range: 1.1 - 1.5
        if self.__localDebug:
            print('heighDiffRelation:', heightDiffRelation)
        return heightDiffRelation


if __name__ == '__main__':
    img = cv2.imread('./PicsEval/B6B.jpg')
    PH = ProjectionHistogram(img)
    if PH.__localDebug:
        print("maxHeightRelation:", PH.checkMaxHeightRelation())
    cv2.imshow('i', img)
    if PH.__localDebug:
        print("Relation between maximums", PH.checkMaximumRelations())
    cv2.waitKey()
    cv2.destroyAllWindows()
