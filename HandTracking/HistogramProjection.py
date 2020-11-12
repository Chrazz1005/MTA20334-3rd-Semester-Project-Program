import numpy as np
import matplotlib.pyplot as plt
import cv2


class HistogramProjection:
    __localDebug = False

    def __init__(self, img):
        self.img = img

    def splitImage(self):
        r, g, b = cv2.split(self.img)

        return r  # Since the image is "binary", being either 0 in all channels or 255, it doesn't matter which channel is returned

    def getHistogram_VProjection(self):  ### Gets a vertical projection of the white pixel distribution

        img = self.splitImage()
        (hY, wY) = img.shape[:2]
        sumColsY = []

        # Creates a list containing the sum of the pixels in each column
        for j in range(hY):
            colY = img[j:j + 1,
                   0:wY]  # since python is (y, x), the y increments 1 each iteration, whereas the the entire x-row is included to calculate the sum of it.

            sumColsY.append(np.sum(colY))

        if self.__localDebug:
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

    def getHistogram_HProjection(self):  ### Gets a horizontal projection of the white pixel distribution

        img = self.splitImage()
        (hX, wX) = img.shape[:2]
        sumColsX = []

        for j in range(wX):
            colX = img[0:hX, j:j + 1]  # Same as the vertical projection, but with the axis flipped.

            sumColsX.append(np.sum(colX))
        if self.__localDebug:
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

    def trimZeros(self, list):  ##### Removing zeros from (empty space) from the data set
        trimmedvert = []
        for i in range(0, len(list)):
            if list[i] != 0:
                trimmedvert.append(list[i])

        return trimmedvert

    def checkDuplicates(self, list):  ############## To be deleted perhaps ##########
        checked = []
        duplicates = []

        for k in range(len(list)):
            if list[k] not in checked:
                checked.append(list[k])
            else:
                duplicates.append(list[k])

        # print('Duplicates:', duplicates)
        return checked

    def getTopXPercentile(self, list, percentile):  ########### To be deleted perhaps #########
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

        maxHori = max(trimHori)
        maxVert = max(trimVert)
        maxHeightRelation = maxVert / maxHori
        if self.__localDebug:
            print('Median of Vertical distribution:', trimVert[int(len(trimVert) / 2)])
            print('Placement of Median:', trimVert.index(trimVert[int(len(trimVert) / 2)]))
            print('----------------------------------------------------')
            print('Median of Horizontal distribution:', trimHori[int(len(trimHori) / 2)])
            print('Placement of Median:', trimHori.index(trimHori[int(len(trimHori) / 2)]))
            print('----------------------------------------------------')
            print('Mean value of vertA:', np.mean(trimVert))
            print('70% of Mean:', np.mean(trimVert) * 0.75)
            print('value 10% in', trimVert[int(len(trimVert) * 0.10)])
            print('----------------------------------------------------')
            print('Forhold mellem største højde i de to histrogrammer', maxHeightRelation)

        if 0.35 < maxHeightRelation < 0.6:
            aScore += 1
            if self.__localDebug:
                print('aScore from relation between max heights of the two distributions')

        lenHori = len(trimHori)
        lenVert = len(trimVert)
        distRatioHori = maxHori / lenHori
        distRatioVert = maxVert / lenVert
        if self.__localDebug:
            print('distRatioHori:', distRatioHori)
            print('distRatioVert:', distRatioVert)

        if 300 <= distRatioHori <= 500 and 95 <= distRatioVert <= 150:
            aScore += 1
            if self.__localDebug:
                print('aScore from ratios of max height and length of the two distributions')

        medianHori = trimHori[int(len(trimHori) / 2)]
        if medianHori > max(trimHori) * 0.90:
            aScore += 1
            if self.__localDebug:
                print('aScore from median being in the top 90%')

        lengRelation = len(trimVert) / len(trimHori)
        if 1.4 < lengRelation < 2.1:
            aScore += 1
            if self.__localDebug:
                print('aScore from relationship between vertical and horizontal length')

        print('aScore:', aScore)
        return aScore

    def checkIfB(self, listvert, listhori):
        trimmedVert = self.trimZeros(listvert)
        trimmedHori = self.trimZeros(listhori)
        bScore = 0

        lenVert = len(trimmedVert)
        lenHori = len(trimmedHori)

        if self.__localDebug:
            print('----------------------------------------------------')
            print('lenVert:', lenVert)
            print('lenHori:', lenHori)
            print('----------------------------------------------------')
            print('biggest val / len(hori):', max(trimmedHori) / len(trimmedHori))
            print('biggest val vert:', max(trimmedVert))
            print('biggest val vert place:', trimmedVert.index(max(trimmedVert)))

        if trimmedVert.index(max(trimmedVert)) < len(trimmedVert) * 0.25:
            bScore += 1
            if self.__localDebug:
                print('bScore from toppoint being placed in first 25% of distribution')

        topLenRelation = max(trimmedHori) / len(
            trimmedHori)  ###Relation between the toppoint and the length of the horizontal distribution
        if 280 < topLenRelation < 310:
            bScore += 1
            if self.__localDebug:
                print('bScore from relation between the toppoint and the length of the horizontal distribution')

        maxHeightRelation = max(trimmedVert) / max(trimmedHori)
        if 0.6 <= maxHeightRelation <= 0.8:
            bScore += 1
            if self.__localDebug:
                print('bScore from relation between max values in the two distributions')

        for i in range(0, int(len(trimmedVert) * 0.30)):
            # print('Første 30%:', trimmedvertvert[i])
            if trimmedVert[i] == max(trimmedVert[0:int(len(trimmedVert) * 0.30)]):
                # print('Første 30% toppunktplacement:', trimmedVert.index(trimmedVert[i]))
                # print('Første 30% toppunkt value:', trimmedVert[i])
                firstTop = [trimmedVert.index(trimmedVert[i]), trimmedVert[i]]

        for i in range(int(len(trimmedVert) * 0.30), len(trimmedVert)):

            if trimmedVert[i] == max(trimmedVert[int(len(trimmedVert) * 0.30):len(trimmedVert)]):
                # print('Sidste 70 % toppunktplacement:', trimmedVert.index(trimmedVert[i]))
                # print('Sidste 70 % toppunkt value:', trimmedVert[i])

                secondTop = [trimmedVert.index(trimmedVert[i]), trimmedVert[i]]

        distTops = secondTop[0] - firstTop[0]
        distTopsnLengthRelation = distTops / len(trimmedVert)
        if 0.18 <= distTopsnLengthRelation <= 0.32:
            bScore += 1
            if self.__localDebug:
                print('bScore from relation between first two tops and the full length of the distribution')

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
        heightDiffRelation = storTop[1] / lilleTop[1]
        heightLengthRelation = storTop[1] / len(trimmedvert)
        if self.__localDebug:
            print('stortop', storTop)
            print('lilletop', lilleTop)
            print('----------------------------------------------------')
            print('Afstand mellem toppunkter:', dstTops)
            print('Forhold mellem afstand og samlede længde:', dstTopsnLengthRelation)
            print('Forhold mellem afstand af toppunkter:', topRelation)
            print('----------------------------------------------------')
            print('Forhold mellem højde:', heightDiffRelation)
            print('Forhold mellem største højde ift. længde', heightLengthRelation)

        if 0.50 < dstTopsnLengthRelation < 0.75:
            cScore += 1
            if self.__localDebug:
                print('cScore from dstTopsnLengthRelation')

        if 1.8 < heightDiffRelation < 2.2:
            cScore += 1
            if self.__localDebug:
                print('cScore from heightDiffRelation')

        if 240 < heightLengthRelation < 260:
            cScore += 1
            if self.__localDebug:
                print('cScore from heightLengthRelation')

        val33 = trimmedhori[int(len(trimmedhori) * 0.33)]
        val50 = trimmedhori[int(len(trimmedhori) * 0.50)]
        val66 = trimmedhori[int(len(trimmedhori) * 0.66)]
        if self.__localDebug:
            print('first 33%', len(trimmedhori) * 0.33)
            print("33% value", trimmedhori[int(len(trimmedhori) * 0.33)])
            print('----------------------------------------------------')
            print('first 50%', len(trimmedhori) * 0.50)
            print(("50% value", trimmedhori[int(len(trimmedhori) * 0.50)]))
            print('----------------------------------------------------')
            print('first 66%', len(trimmedhori) * 0.66)
            print(("66% value", trimmedhori[int(len(trimmedhori) * 0.66)]))

        if val33 + val33 * 0.25 < val50 > val66 + val66 * 0.25:
            cScore += 1
            if self.__localDebug:
                print('cScore for increase and decrease in right intervals')

        maxHeightRelation = max(trimmedvert) / max(trimmedhori)
        if 1.1 < maxHeightRelation < 1.4:
            cScore += 1
            if self.__localDebug:
                print('cScore from relation between max heights of the two distributions')

        print('cScore:', cScore)
        return cScore

    def checkGesture(self):
        verticalDist = self.getHistogram_VProjection()
        horizontalDist = self.getHistogram_HProjection()

        finalAScore = self.checkIfA(verticalDist, horizontalDist)
        finalBScore = self.checkIfB(verticalDist, horizontalDist)
        finalCScore = self.checkIfC(verticalDist, horizontalDist)
        if finalAScore > finalBScore and finalAScore > finalCScore:
            print('Gesture is A')

        if finalBScore > finalAScore and finalBScore > finalCScore:
            print('Gesture is B')

        if finalCScore > finalAScore and finalCScore > finalBScore:
            print('Gesture is C')


if __name__ == '__main__':
    imgA = cv2.imread('./PicsEval/C6B.jpg')
    imgA2 = cv2.imread('./PicsEval/A5B.jpg')
    imgA3 = cv2.imread('./PicsEval/A6B.jpg')

    imgB = cv2.imread('./PicsEval/B3B.jpg')
    imgB2 = cv2.imread('./PicsEval/B4B.jpg')
    imgB3 = cv2.imread('./PicsEval/B6B.jpg')
    imgC = cv2.imread('./PicsEval/C4B.jpg')
    imgC2 = cv2.imread('./PicsEval/C1B.jpg')

    ProjectDist = HistogramProjection(imgA)
    ProjectDist.checkGesture()

    # cv2.imshow('C', imgC)
    # cv2.imshow('A', imgA)
    # cv2.imshow('B', imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
