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

        print('Vertical distribution:', sumColsY)
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

        print('Horizontal distribution:', sumColsX)
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

    def checkIfA(self, listVert, listHori):
        trimVert = self.trimZeros(listVert)
        trimHori = self.trimZeros(listHori)

        aScore = 0

        lengDiff = len(trimVert) - len(trimHori)
        lengRelation = len(trimVert) / len(trimHori)
        print('----------------------------------------------------')
        print('Længde af Hori', len(trimHori))
        print('Længde af Vert', len(trimVert))
        print('Forskel mellem Hori længde (håndbredde) og Vert længde (Håndlængde):', lengDiff)
        print('Forhold mellem Hori længde (håndbredde) og Vert længde (Håndlængde):', lengRelation)
        print('----------------------------------------------------')
        print('Median of Vertical distribution:', trimVert[int(len(trimVert) / 2)])
        print('Placement of Median:', trimVert.index(trimVert[int(len(trimVert) / 2)]))
        print('Median:', trimVert[int(len(trimVert) / 2)])
        print('----------------------------------------------------')
        print('Median of Vertical distribution:', trimHori[int(len(trimHori) / 2)])
        print('Placement of Median:', trimHori.index(trimHori[int(len(trimHori) / 2)]))
        print('Median:', trimHori[int(len(trimHori) / 2)])
        medianHori = trimHori[int(len(trimHori) / 2)]
        print('----------------------------------------------------')
        maxHeightRelation = max(trimVert) / max(trimHori)
        print('Forhold mellem største højde i de to histrogrammer', maxHeightRelation)

        print('Mean value of vertA:', np.mean(trimVert))
        print('70% of Mean:', np.mean(trimVert) * 0.70)
        mean70p = np.mean(trimVert) * 0.70
        print('value 10% in', trimVert[int(len(trimVert) * 0.10)])


        for s in range(int(len(trimVert) * 0.10), len(trimVert)): ###Denne parameter er gældene for alle tre håndtegn så den skal laves om
            if trimVert[s] < mean70p:
                isA = False

            else:
                isA = True

        if isA == True:
            aScore += 1
            print('bScore from steady course throughout vertical distribution')

        if medianHori > max(trimHori) * 0.80:
            aScore += 1
            print('bScore from median being in the top 90%')

        if 1.7 < lengRelation < 2.2:
            aScore += 1
            print('bScore from relationship between vertical and horizontal length')

        print('bScore:', aScore)
        return aScore

    def checkIfC(self, list):
        #### Karaktaristika for C;
        # - To toppunkter af relativ højde til hinanden
        # - Toppunkter af relativ højde til de omkringliggende
        # - Toppunkter er af relativ afstand til hinanden

        trimmed = self.trimZeros(list)  # Removing 0's
        cScore = 0

        # print('first 30%', len(trimmed) * 0.30)
        # print('first 40%', len(trimmed) * 0.40)
        # print('first 50%', len(trimmed) * 0.50)
        # print('first 80%', len(trimmed) * 0.80)
        # print('Listen', len(list))
        # print('Trimmed', len(trimmed))

        for i in range(0, int(len(trimmed) * 0.30)):
            # print('Første 30%:', trimmed[i])
            if trimmed[i] == max(trimmed[0:int(len(trimmed) * 0.30)]):
                print('toppunktplacement:', trimmed.index(trimmed[i]))
                lilleTop = [trimmed.index(trimmed[i]), trimmed[i]]

        for i in range(int(len(trimmed) * 0.30), len(trimmed)):
            # print('Sidste 70%:', trimmed[i])
            if trimmed[i] == max(trimmed[int(len(trimmed) * 0.30):len(trimmed)]):
                print('toppunktplacement:', trimmed.index(trimmed[i]))
                storTop = [trimmed.index(trimmed[i]), trimmed[i]]

        dstTops = storTop[0] - lilleTop[0]
        dstTopsnLengthRelation = dstTops / len(trimmed)

        print('Afstand mellem toppunkter:', dstTops)
        print('Forhold mellem afstand og samlede længde:', dstTopsnLengthRelation)

        heightDiffRelation = storTop[1] / lilleTop[1]
        heightLengthRelation = storTop[1] / len(trimmed)

        print('Forhold mellem højde:', heightDiffRelation)
        print('Forhold mellem største højde ift. længde', heightLengthRelation)

        if 0.30 < dstTopsnLengthRelation < 0.50:
            cScore += 1
            print('cScore from dstTopsnLengthRelation')

        if 1.3 < heightDiffRelation < 2.0:
            cScore += 1
            print('cScore from heightDiffRelation')

        if 160 < heightLengthRelation < 180:
            cScore += 1
            print('cScore from heightLengthRelation')

        print('cScore:', cScore)
        return cScore


if __name__ == '__main__':
    imgB = cv2.imread('binaryB.png')
    imgC = cv2.imread('binaryC.png')
    imgA = cv2.imread('binary.png')

    ProjectDist = HistogramProjection(imgC)
    horizontalDistC = ProjectDist.getHistogram_HProjection()
    verticalDistC = ProjectDist.getHistogram_VProjection()


    ProjectDistB = HistogramProjection(imgB)
    verticalB = ProjectDistB.getHistogram_HProjection()
    horizB = ProjectDistB.getHistogram_VProjection()


    ProjectDistA = HistogramProjection(imgA)
    vertA = ProjectDistA.getHistogram_VProjection()
    horizA = ProjectDistA.getHistogram_HProjection()
    

    # cv2.imshow('C', imgC)
    cv2.imshow('A', imgA)
    # cv2.imshow('B', imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
