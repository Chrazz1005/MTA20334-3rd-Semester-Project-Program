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

    def checkDuplicates(self, list):
        check = []
        duplicates = []

        for k in range(len(list)):
            if list[k] not in check:
                check.append(list[k])
            else:
                duplicates.append(list[k])

        print('Duplicates:', duplicates)
        return check

    def checkRelativePos(self, list):
        groups = {}   ##Group number : Height
        gNumber = 0

        groups[gNumber] = list[0][0]
        for z in range(len(list)):
            if int(list[z][1]) + 10 > list[z + 1 < len(list)][1]: ###Revise +10 alt efter hvor godt det kommer til at fungere
                groups[gNumber] = list[z + 1 < len(list)][0]

            elif list[z][1] + 10 < list[z + 1 < len(list)][1]:
                gNumber += 1
                groups[gNumber] = list[z + 1 < len(list)][0]

        return groups



    ##Vi skal gruppere hvert interval af toppunkter
    #checke om deres "højde" er nogenlunde lige høje (if højde < 0.70*anden højde: lige høje)
    #if lige høje tæl antal af intervaller
    #if antal =< 3: hånd


if __name__ == '__main__':
    img = cv2.imread('binaryHand.png')

    ProjectDist = HistogramProjection(img)

    horizontalDist = ProjectDist.getHistogram_HProjection()
    # verticalDist = ProjectDist.getHistogram_VProjection()

    print('Median of SumColsX unsorted dataset:', horizontalDist[int(len(horizontalDist) / 2)])
    print('Placement of Median:', horizontalDist.index(horizontalDist[int(len(horizontalDist) / 2)]))
    medianHori = horizontalDist.index(horizontalDist[int(len(horizontalDist) / 2)])

    print('Median + 10%:', horizontalDist[int(medianHori * 1.10)])
    print('Median - 10%:', horizontalDist[int(medianHori * 0.90)])

    toppunkter = []
    for i in range(len(horizontalDist)):
        if horizontalDist[i] > max(horizontalDist) * 0.90:
            toppunkter.append([horizontalDist[i], horizontalDist.index(horizontalDist[i])])

            print('Top 90% value:', horizontalDist[i])
            print('Top 90% placement:', horizontalDist.index(horizontalDist[i]))
            print('-------------------------------------')

    sortToppunkter = ProjectDist.checkDuplicates(toppunkter)

    print('--------------------------------')
    print('Toppunkter unsorted:', toppunkter)
    print('--------------------------------')
    print('Toppunkter sorted:', sortToppunkter)


    print('--------------------------------')

    groupedToppunkter = ProjectDist.checkRelativePos(sortToppunkter)

    print('Grupperede toppunkter:', groupedToppunkter)

    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
