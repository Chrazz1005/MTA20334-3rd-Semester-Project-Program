import numpy as np
import matplotlib.pyplot as plt
import cv2


class HistogramProjection:

    def __init__(self, img):
        self.img = img

    def splitImage(self):
        r, g, b = cv2.split(self.img)

        return r  # Since the image is "binary", being either 0 in all channels or 255, it doesn't matter which channel is returned

    def getHistogram_VProjection(self):
        "Return a list containing the sum of the pixels in each column"
        img = self.splitImage()
        (hY, wY) = img.shape[:2]
        sumColsY = []

        for j in range(hY):
            colY = img[j:j + 1, 0:wY]  # y1:y2, x1:x2

            sumColsY.append(np.sum(colY))

        print(sumColsY)
        print('length vertical array:', len(sumColsY))
        x_axis = []
        for i in range(0, img.shape[0]):
            x_axis.append(i)


        plt.xlabel('Pixel No. (ranging from 0 to the length of y-axis of the image)')
        plt.ylabel('Sum of white pixels in row y')
        plt.title('Vertical distribution', fontsize=15)
        plt.plot(x_axis, sumColsY)
        plt.show()

        return sumColsY

    def getHistogram_HProjection(self):
        "Return a list containing the sum of the pixels in each column"
        img = self.splitImage()
        (hX, wX) = img.shape[:2]
        sumColsX = []

        for j in range(wX):
            colX = img[0:hX, j:j + 1]  # y1:y2, x1:x2

            sumColsX.append(np.sum(colX))

        # print(sumColsX)
        print('length horizontal array:', len(sumColsX))
        x_axis = []
        for a in range(0, img.shape[1]):
            x_axis.append(a)

        plt.xlabel('Pixel No. (ranging from 0 to the length of x-axis of the image)')
        plt.ylabel('Sum of white pixels in col x')
        plt.title('Horizontal distribution', fontsize=15)
        plt.plot(x_axis, sumColsX)
        plt.show()

        return sumColsX

    def trimZeros(self, list):
        trimmed = []
        for i in range(0, len(list)):
            if list[i] != 0:
                trimmed.append(list[i])

        return trimmed

    def checkDuplicates(self, list):
        checked = []
        duplicates = []

        for k in range(len(list)):
            if list[k] not in checked:
                checked.append(list[k])
            else:
                duplicates.append(list[k])

        # print('Duplicates:', duplicates)
        return checked

    def checkRelativePos(self, list):
        groups = []  ##Group number : Height
        gNumber = 0

        print('Groups pre-loop', groups)

        for z in range(len(list)):

            if list[z][1] < list[z + 1 < len(list)][
                1] + 10:  #### Revise +10 alt efter hvor godt det kommer til at fungere
                print('Groups first ifloop', groups)
                groups.append([list[z][0], gNumber])

            elif list[z][1] > list[z + 1 < len(list)][1] + 10:
                gNumber += 1
                print('Groups second ifloop', groups)
                groups.append([list[z][0], gNumber])

        return groups

    def getTopXPercentile(self, list, percentile):
        toppunkter = []
        for i in range(len(list)):
            if list[i] > max(list) * int(percentile / 100):
                toppunkter.append([list[i], list.index(list[i])])
                # print('Top 90% values:', list[i])
                # print('-------------------------------------')
                # print('Top 90% placement:', list.index(list[i]))
                # print('-------------------------------------')

        sortToppunkter = self.checkDuplicates(toppunkter)

        return sortToppunkter

    def checkIfC(self, list):
        #### Karaktaristika for C;
        # - To toppunkter af relativ højde til hinanden
        # - Toppunkter af relativ højde til de omkringliggende
        # - Toppunkter er af relativ afstand til hinanden

        trimmed = self.trimZeros(list)

        firstPoint = []
        print('first 30%', len(trimmed) * 0.30)
        print('first 40%', len(trimmed) * 0.40)
        print('first 50%', len(trimmed) * 0.50)
        print('first 80%', len(trimmed) * 0.80)
        print('Listen', len(list))
        print('Trimmed', len(trimmed))

        for i in range(int(len(trimmed)*0.20), len(trimmed)):
            print('Sidste 80%:', trimmed[i])
            if trimmed[i] == max(trimmed):
                print('toppunktplacement', trimmed.index(trimmed[i]))

        # for i in range(0, len(trimmed)):
        #     if int(len(trimmed)*0.20) > trimmed[i]:
        #         firstPoint.append(trimmed[i])
        #
        #




if __name__ == '__main__':
    imgB = cv2.imread('binaryB.png')
    imgC = cv2.imread('binaryC.png')
    imgA = cv2.imread('binary.png')

    ProjectDist = HistogramProjection(imgC)
    horizontalDist = ProjectDist.getHistogram_HProjection()

    verticalDist = ProjectDist.getHistogram_VProjection()

    # ProjectDistA = HistogramProjection(imgA)
    # vertiDistC = ProjectDistA.getHistogram_VProjection()
    # horiDistC = ProjectDistA.getHistogram_HProjection()
    #
    # ProjectDistB = HistogramProjection(imgB)
    # horiDistB = ProjectDistB.getHistogram_HProjection()
    # vertiDistB = ProjectDistB.getHistogram_VProjection()

    print('Median of SumColsX unsorted dataset:', verticalDist[int(len(verticalDist) / 2)])
    print('Placement of Median:', verticalDist.index(verticalDist[int(len(verticalDist) / 2)]))
    medianHori = verticalDist.index(verticalDist[int(len(verticalDist) / 2)])

    print('Median + 10%:', verticalDist[int(medianHori * 1.10)])
    print('Median - 10%:', verticalDist[int(medianHori * 0.90)])



    ProjectDist.checkIfC(verticalDist)


    cv2.imshow('C', imgC)
    # cv2.imshow('A', imgA)
    # cv2.imshow('B', imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
