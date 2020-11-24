import time

import cv2
import numpy as np


class GrassFire:

    def __init__(self, img):
        self.img = img
        self.img_height = self.img.shape[0]  # 0 = height
        self.img_width = self.img.shape[1]  # 1 = width
        self.blob_number = 0  # assigns a number to each blob
        self.arr = np.array([])
        self.queue = []
        self.blob_number_greatest = 0  # number of the greatest blob

    def outputSize(self):
        outputSizeTime = time.time()
        self.arr = np.array([[0] * self.img_width for i in range(0, self.img_height)])  # height x width list of zeros
        #print("GrassFire: outputSize time: %s" % round((time.time() - outputSizeTime), 2), "seconds")
        return self.arr

    def grassFire(self, img):
        grassFireTime = time.time()
        for y in range(0, self.img_height):
            for x in range(0, self.img_width):

                current_pos = [y, x]
                pos1 = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                pos2 = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                pos3 = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                pos4 = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                current_value = img[y, x]

                # If queue is empty, search for new blobs.
                if len(self.queue) == 0:

                    # If a white pixel is found and has not already been found, start grass-fire search
                    if current_value != 0:
                        self.blob_number += 1
                        self.arr[current_pos[0]][current_pos[1]] = self.blob_number
                        img[y, x] = 0

                        # Grass-fire search begins
                        if current_pos[1] < self.img_width - 1:  # If x < image width
                            pos1_value = img[y, x + 1]  # px value to the right
                            # Searching east...
                            if pos1_value != 0:
                                self.arr[pos1[0]][pos1[1]] = self.blob_number
                                self.queue.append(pos1)
                                img[pos1[0], pos1[1]] = 0

                        if current_pos[0] < self.img_height - 1:
                            pos2_value = img[y + 1, x]  # px value below
                            # Searching south...
                            if pos2_value != 0:
                                self.arr[pos2[0]][pos2[1]] = self.blob_number
                                self.queue.append(pos2)
                                img[pos2[0], pos2[1]] = 0

                        if current_pos[1] > 0:
                            pos3_value = img[y, x - 1]  # px value to the left
                            # Searching west...
                            if pos3_value != 0:
                                self.arr[pos2[0]][pos2[1]] = self.blob_number
                                self.queue.append(pos3)
                                img[pos3[0], pos3[1]] = 0

                        if current_pos[0] > 0:
                            pos4_value = img[y - 1, x]  # px value above
                            # Searching north...
                            if pos4_value != 0:
                                self.arr[y - 1][x] = self.blob_number
                                self.queue.append(pos4)
                                img[pos4[0], pos4[1]] = 0

                # If que is not empty, continue searching for pixels in the current blob.
                for i in range(0, len(self.queue)):
                    current_pos = self.queue[0]

                    pos1 = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                    pos2 = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                    pos3 = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                    pos4 = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                    # Grass-fire search
                    if current_pos[1] < self.img_width - 1:
                        pos1_value = img[pos1[0], pos1[1]]  # px value to the right
                        # Searching east...
                        if pos1_value != 0:
                            self.arr[pos1[0]][pos1[1]] = self.blob_number
                            self.queue.append(pos1)
                            img[pos1[0], pos1[1]] = 0

                    if current_pos[0] < self.img_height - 1:
                        pos2_value = img[pos2[0], pos2[1]]  # px value below
                        # Searching south...
                        if pos2_value != 0:
                            self.arr[pos2[0]][pos2[1]] = self.blob_number
                            self.queue.append(pos2)
                            img[pos2[0], pos2[1]] = 0

                    if current_pos[1] > 0:
                        pos3_value = img[pos3[0], pos3[1]]  # px value to the left
                        # Searching west...
                        if pos3_value != 0:
                            self.arr[pos3[0]][pos3[1]] = self.blob_number
                            self.queue.append(pos3)
                            img[pos3[0], pos3[1]] = 0

                    if current_pos[0] > 0:
                        pos4_value = img[pos4[0], pos4[1]]  # px value above
                        # Searching north...
                        if pos4_value != 0:
                            self.arr[pos4[0]][pos4[1]] = self.blob_number
                            self.queue.append(pos4)
                            img[pos4[0], pos4[1]] = 0

                    self.queue.remove(self.queue[0])

        # ¤print("Grass-fire is done.")

        # for y in self.arr:
        #    print(y)
        #print("GrassFire: GrassFire time: %s" % round((time.time() - grassFireTime), 2), "seconds")

        return self.arr

    def greatestBlob(self):
        greatestBlobTime = time.time()
        greatest_blob = 0

        # Finds the greatest blob
        for j in range(1, self.blob_number + 1):
            blob_size = len(self.arr[self.arr == j])
            if blob_size > greatest_blob:
                greatest_blob = blob_size
                self.blob_number_greatest = j

        # When the value is not the number of the greatest blob, change to zero.
        self.arr[self.arr != self.blob_number_greatest] = 0
        # Change the number to 1, such that the array consists of 0's and 1's, where 1 is the greatest blob.
        self.arr = self.arr / self.blob_number_greatest
        #print("GrassFire: greatestBlob time: %s" % round((time.time() - greatestBlobTime), 2), "seconds")

        return self.arr

    # recolors the image based on the binary output list, such that only the greatest blob remains.

    def outputImage(self):
        # img[y, x] = pixel value, 0 or 255
        # self.arr[y][x] = value in output list, 0 or 1
        outputImageTime = time.time()
        # searches through the image image.
        for y in range(0, self.img_height):
            for x in range(0, self.img_width):
                # if the pixel value is not black and the value in the output list is black, change the pixel value
                # in the image to black.
                if self.img[y, x] != 0 and self.arr[y][x] == 0:
                    self.img[y, x] = 0
                if self.img[y, x] != 255 and self.arr[y][x] == 1:
                    self.img[y, x] = 255
        #print("GrassFire: outputImage time: %s" % round((time.time() - outputImageTime), 2), "seconds")

    def startGrassFire(self):
        totalTime = time.time()
        self.outputSize()
        self.grassFire(self.img)
        self.greatestBlob()
        #self.outputImage()
        #print("GrassFire: Total time: %s" % round((time.time() - totalTime), 2), "seconds")
        return self.arr
