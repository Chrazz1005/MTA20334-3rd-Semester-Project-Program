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
        trimmedvert = []
        for i in range(0, len(list)):
            if list[i] != 0:
                trimmedvert.append(list[i])

        return trimmedvert

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

    def getTopXPercentile(self, list, percentile):
        toppunkter = []
        for i in range(len(list)):
            if list[i] > max(list) * percentile / 100:
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

        lengRelation = len(trimVert) / len(trimHori)
        print('----------------------------------------------------')
        print('Forhold mellem Hori længde (håndbredde) og Vert længde (Håndlængde):', lengRelation)
        print('----------------------------------------------------')
        print('Median of Vertical distribution:', trimVert[int(len(trimVert) / 2)])
        print('Placement of Median:', trimVert.index(trimVert[int(len(trimVert) / 2)]))
        print('----------------------------------------------------')
        print('Median of Horizontal distribution:', trimHori[int(len(trimHori) / 2)])
        print('Placement of Median:', trimHori.index(trimHori[int(len(trimHori) / 2)]))
        medianHori = trimHori[int(len(trimHori) / 2)]
        print('----------------------------------------------------')
        print('Mean value of vertA:', np.mean(trimVert))
        print('70% of Mean:', np.mean(trimVert) * 0.75)
        print('value 10% in', trimVert[int(len(trimVert) * 0.10)])
        maxHeightRelation = max(trimVert) / max(trimHori)
        print('Forhold mellem største højde i de to histrogrammer', maxHeightRelation)
        if 0.35 < maxHeightRelation < 0.45:
            aScore += 1
            print('aScore from relation between max heights of the two distributions')

        if medianHori > max(trimHori) * 0.98:
            aScore += 1
            print('aScore from median being in the top 98%')

        if 1.7 < lengRelation < 2.2:
            aScore += 1
            print('aScore from relationship between vertical and horizontal length')

        print('aScore:', aScore)
        return aScore

    def checkifB(self, listvert, listhori):
        trimmedVert = self.trimZeros(listvert)
        trimmedHori = self.trimZeros(listhori)
        bScore = 0

        lenVert = len(trimmedVert)
        lenHori = len(trimmedHori)

        print('lenVert:', lenVert)
        print('lenHori:', lenHori)

        print('biggest val / len(hori):', max(trimmedHori) / len(trimmedHori))

        print('biggest val vert:', max(trimmedVert))
        print('biggest val vert place:', trimmedVert.index(max(trimmedVert)))
        if trimmedVert.index(max(trimmedVert)) < len(trimmedVert) * 0.25:
            bScore += 1
            print('bScore from toppoint being placed in first 25% of distribution')

        topLenRelation = max(trimmedHori) / len(
            trimmedHori)  ###Relation between the toppoint and the length of the horizontal distribution
        if 280 < topLenRelation < 310:
            bScore += 1
            print('bScore from relation between the toppoint and the length of the horizontal distribution')


        ######################## Du mangler lige en sidste til B ################

        maxHeightRelation = max(trimmedVert) / max(trimmedHori)
        if 0.6 <= maxHeightRelation <= 0.8:
            bScore += 1
            print('bScore from relation between max values in the two distributions')

        print('top85 cluster', self.getTopXPercentile(trimmedHori, 85))
        print('len top85 cluster', len(self.getTopXPercentile(trimmedHori, 85)))
        top85cluster = self.getTopXPercentile(trimmedHori, 85)
        lenTop85cluster = len(top85cluster)

        print('bScore:', bScore)
        return bScore

    def checkIfC(self, listvert, listhori):
        #### Karaktaristika for C;
        # - To toppunkter af relativ højde til hinanden
        # - Toppunkter af relativ højde til de omkringliggende
        # - Toppunkter er af relativ afstand til hinanden

        trimmedvert = self.trimZeros(listvert)  # Removing 0's
        trimmedhori = self.trimZeros(listhori)
        cScore = 0

        for i in range(0, int(len(trimmedvert) * 0.30)):
            # print('Første 30%:', trimmedvertvert[i])
            if trimmedvert[i] == max(trimmedvert[0:int(len(trimmedvert) * 0.30)]):
                # print('Første 30% toppunktplacement:', trimmedvert.index(trimmedvert[i]))
                # print('Første 30% toppunkt valye:', trimmedvert[i])
                lilleTop = [trimmedvert.index(trimmedvert[i]), trimmedvert[i]]

        for i in range(int(len(trimmedvert) * 0.30), len(trimmedvert)):

            if trimmedvert[i] == max(trimmedvert[int(len(trimmedvert) * 0.30):len(trimmedvert)]):
                # print('Sidste 70 % toppunktplacement:', trimmedvert.index(trimmedvert[i]))
                # print('Sidste 70 % toppunkt value:', trimmedvert[i])

                storTop = [trimmedvert.index(trimmedvert[i]), trimmedvert[i]]

        dstTops = storTop[0] - lilleTop[0]
        dstTopsnLengthRelation = dstTops / len(trimmedvert)
        topRelation = storTop[0] / lilleTop[0]
        print('stortop', storTop)
        print('lilletop', lilleTop)
        print('Afstand mellem toppunkter:', dstTops)
        print('Forhold mellem afstand og samlede længde:', dstTopsnLengthRelation)
        print('Forhold mellem afstand af toppunkter:', topRelation)

        heightDiffRelation = storTop[1] / lilleTop[1]
        heightLengthRelation = storTop[1] / len(trimmedvert)

        print('Forhold mellem højde:', heightDiffRelation)
        print('Forhold mellem største højde ift. længde', heightLengthRelation)

        if 0.50 < dstTopsnLengthRelation < 0.75:
            cScore += 1
            print('cScore from dstTopsnLengthRelation')

        if 1.8 < heightDiffRelation < 2.2:
            cScore += 1
            print('cScore from heightDiffRelation')

        if 240 < heightLengthRelation < 260:
            cScore += 1
            print('cScore from heightLengthRelation')

        print('first 33%', len(trimmedhori) * 0.33)
        print("33% value", trimmedhori[int(len(trimmedhori) * 0.33)])
        val33 = trimmedhori[int(len(trimmedhori) * 0.33)]
        print('first 50%', len(trimmedhori) * 0.50)
        print(("50% value", trimmedhori[int(len(trimmedhori) * 0.50)]))
        val50 = trimmedhori[int(len(trimmedhori) * 0.50)]
        print('first 66%', len(trimmedhori) * 0.66)
        print(("66% value", trimmedhori[int(len(trimmedhori) * 0.66)]))
        val66 = trimmedhori[int(len(trimmedhori) * 0.66)]

        if val33 + val33 * 0.25 < val50 > val66 + val66 * 0.25:
            cScore += 1
            print('cScore for increase and decrease in right intervals')

        maxHeightRelation = max(trimmedvert) / max(trimmedhori)
        print('Forhold mellem største højde i de to histrogrammer', maxHeightRelation)
        if 1.1 < maxHeightRelation < 1.4:
            cScore += 1
            print('cScore from relation between max heights of the two distributions')

        print('cScore:', cScore)
        return cScore


if __name__ == '__main__':
    imgA = cv2.imread('./PicsEval/A5B.jpg')
    imgB = cv2.imread('./PicsEval/B3B.jpg')
    imgB2 = cv2.imread('./PicsEval/B4B.jpg')
    imgB3 = cv2.imread('./PicsEval/B6B.jpg')
    imgC = cv2.imread('./PicsEval/C4B.jpg')
    imgC2 = cv2.imread('./PicsEval/C6B.jpg')

    # ProjectDistA = HistogramProjection(imgA)
    # vertA = ProjectDistA.getHistogram_VProjection()
    # horizA = ProjectDistA.getHistogram_HProjection()
    # ProjectDistA.checkIfA(vertA, horizA)
    # ProjectDistA.checkifB(vertA, horizA)
    # ProjectDistA.checkIfC(vertA, horizA)

    ProjectDistB = HistogramProjection(imgB)
    verticalB = ProjectDistB.getHistogram_VProjection()
    horizB = ProjectDistB.getHistogram_HProjection()
    ProjectDistB.checkIfA(verticalB, horizB)
    ProjectDistB.checkifB(verticalB, horizB)
    ProjectDistB.checkIfC(verticalB, horizB)

    ProjectDistB = HistogramProjection(imgB2)
    verticalB = ProjectDistB.getHistogram_VProjection()
    horizB = ProjectDistB.getHistogram_HProjection()
    ProjectDistB.checkIfA(verticalB, horizB)
    ProjectDistB.checkifB(verticalB, horizB)
    ProjectDistB.checkIfC(verticalB, horizB)

    ProjectDistB = HistogramProjection(imgB3)
    verticalB = ProjectDistB.getHistogram_VProjection()
    horizB = ProjectDistB.getHistogram_HProjection()
    ProjectDistB.checkIfA(verticalB, horizB)
    ProjectDistB.checkifB(verticalB, horizB)
    ProjectDistB.checkIfC(verticalB, horizB)

    # ProjectdistC2 = HistogramProjection(imgC2)
    # horidistC2 = ProjectdistC2.getHistogram_HProjection()
    # vertidistC2 = ProjectdistC2.getHistogram_VProjection()
    # ProjectdistC2.checkIfA(vertidistC2, horidistC2)
    # ProjectdistC2.checkifB(vertidistC2, horidistC2)
    # ProjectdistC2.checkIfC(vertidistC2, horidistC2)
    #
    # ProjectDistC = HistogramProjection(imgC)
    # horizontalDistC = ProjectDistC.getHistogram_HProjection()
    # verticalDistC = ProjectDistC.getHistogram_VProjection()
    # ProjectDistC.checkIfA(verticalDistC, horizontalDistC)
    # ProjectDistC.checkifB(verticalDistC, horizontalDistC)
    # ProjectDistC.checkIfC(verticalDistC, horizontalDistC)

    # cv2.imshow('C', imgC)
    # cv2.imshow('A', imgA)
    # cv2.imshow('B', imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
