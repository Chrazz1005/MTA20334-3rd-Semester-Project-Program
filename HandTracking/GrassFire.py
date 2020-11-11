import cv2


class GrassFire:

    def __init__(self, img):
        self.img = img
        self.img_height = self.img.shape[0]  # 0 = height
        self.img_width = self.img.shape[1]   # 1 = width
        self.blob_number = 0     # assigns a number to each blob
        self.output_list = []
        self.queue = []
        self.blob_number_greatest = 0      # number of the greatest blob

    def outputSize(self):
        self.output_list = [[0] * self.img_width for i in range(0, self.img_height)] # height x width list of zeros
        return self.output_list

    def grassFire(self, img):
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
                        self.output_list[current_pos[0]][current_pos[1]] = self.blob_number
                        img[y, x] = 0

                        # Grass-fire search begins
                        if current_pos[1] < self.img_width-1: # If x < image width
                            pos1_value = img[y, x + 1]  # px value to the right
                            # Searching east...
                            if pos1_value != 0:
                                self.output_list[pos1[0]][pos1[1]] = self.blob_number
                                self.queue.append(pos1)
                                img[pos1[0], pos1[1]] = 0

                        if current_pos[0] < self.img_height - 1:
                            pos2_value = img[y + 1, x]  # px value below
                            # Searching south...
                            if pos2_value != 0:
                                self.output_list[pos2[0]][pos2[1]] = self.blob_number
                                self.queue.append(pos2)
                                img[pos2[0], pos2[1]] = 0

                        if current_pos[1] > 0:
                            pos3_value = img[y, x - 1]  # px value to the left
                            #Searching west...
                            if pos3_value != 0:
                                self.output_list[pos2[0]][pos2[1]] = self.blob_number
                                self.queue.append(pos3)
                                img[pos3[0], pos3[1]] = 0

                        if current_pos[0] > 0:
                            pos4_value = img[y - 1, x]  # px value above
                            # Searching north...
                            if pos4_value != 0:
                                self.output_list[y-1][x] = self.blob_number
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
                    if current_pos[1] < self.img_width-1:
                        pos1_value = img[pos1[0], pos1[1]]  # px value to the right
                        # Searching east...
                        if pos1_value != 0:
                            self.output_list[pos1[0]][pos1[1]] = self.blob_number
                            self.queue.append(pos1)
                            img[pos1[0], pos1[1]] = 0

                    if current_pos[0] < self.img_height-1:
                        pos2_value = img[pos2[0], pos2[1]]  # px value below
                        # Searching south...
                        if pos2_value != 0:
                            self.output_list[pos2[0]][pos2[1]] = self.blob_number
                            self.queue.append(pos2)
                            img[pos2[0], pos2[1]] = 0

                    if current_pos[1] > 0:
                        pos3_value = img[pos3[0], pos3[1]]  # px value to the left
                        # Searching west...
                        if pos3_value != 0:
                            self.output_list[pos3[0]][pos3[1]] = self.blob_number
                            self.queue.append(pos3)
                            img[pos3[0], pos3[1]] = 0

                    if current_pos[0] > 0:
                        pos4_value = img[pos4[0], pos4[1]]  # px value above
                        # Searching north...
                        if pos4_value != 0:
                            self.output_list[pos4[0]][pos4[1]] = self.blob_number
                            self.queue.append(pos4)
                            img[pos4[0], pos4[1]] = 0

                    self.queue.remove(self.queue[0])

        print("Grass-fire is done.")

        #for y in self.output_list:
        #    print(y)

        return self.output_list


    def greatestBlob(self):
        greatest_blob = 0

        for j in range(1, self.blob_number+1):
            blob_size = sum(i.count(j) for i in self.output_list) # counts number of each element in list. i = index, j = element.

            if blob_size > greatest_blob:
                greatest_blob = blob_size
                self.blob_number_greatest = j

        return self.blob_number_greatest


    # creates a list containing only 0's and 1's, where 1 is the blob.
    def outputList(self):
        # searches through the output list.
        for y in range(len(self.output_list)):
            for x in range(len(self.output_list[y])):
                # if the value in the output list is not corresponding to the number of the greatest blob, the value is
                # set to 0. Otherwise, set to 1.
                if self.output_list[y][x] != self.blob_number_greatest:
                    self.output_list[y][x] = 0
                else:
                    self.output_list[y][x] = 1
        #
        # for y in self.output_list:
        #     print(y)

        # A list containing only 0's and 1's is returned.
        return self.output_list


    # recolors the image based on the binary output list, such that only the greatest blob remains.
    def outputImage(self):
        # img[y, x] = pixel value, 0 or 255
        # self.output_list[y][x] = value in output list, 0 or 1

        #searches through the image image.
        for y in range(0, self.img_height):
            for x in range(0, self.img_width):
                # if the pixel value is not black and the value in the output list is black, change the pixel value
                # in the image to black.
                if self.img[y, x] != 0 and self.output_list[y][x] == 0:
                    self.img[y, x] = 0
                if self.img[y, x] != 255 and self.output_list[y][x] == 1:
                    self.img[y, x] = 255


    def startGrassFire(self):
        self.outputSize()
        self.grassFire(self.img)
        self.greatestBlob()
        self.outputList()
        self.outputImage()
        return self.img

