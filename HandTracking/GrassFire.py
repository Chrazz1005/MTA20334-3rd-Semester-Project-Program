import cv2


class GrassFire:
    def __init__(self, img):
        self.img = img
        self.img_height = self.img.shape[0]  # 0 = height
        self.img_width = self.img.shape[1]  # 1 = width

        self.list_length = self.img_width * self.img_height  # total number of pixels in image

        self.blob_number = 0  # assigns a number to each blob
        self.output_list = [[0] * self.img_height for i in range(0, self.img_width)]  # height x width list of zeros

        self.queue = []
        self.white_pixels = []  # contains coordinates of each white pixel
        self.black_pixels = []  # contains coordinates of each black pixel
        self.blob_number_greatest = 0  # number of the greatest blob


    def outputSize(self):
        self.output_list = [[0] * self.img_width for i in range(0, self.img_height)] # height x width list of zeros
        return self.output_list

    def grassFire(self, img):

        for y in range(0, self.img_height):
            for x in range(0, self.img_width):

                current_pos = [y, x]
                pos1_coordinates = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                pos2_coordinates = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                pos3_coordinates = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                pos4_coordinates = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                current_value = img[y, x]

                # If queue is empty, search for new blobs.
                if len(self.queue) == 0:

                    # If a white pixel is found and has not already been found, start grass-fire search
                    if current_value != 0 and current_pos not in self.white_pixels:
                        self.white_pixels.append(current_pos)
                        self.blob_number += 1
                        self.output_list[current_pos[0]][current_pos[1]] = self.blob_number
                        #print("\nFound BLOB", self.blob_number, "at:", current_pos)

                        # Grass-fire search begins
                        if current_pos[1] < self.img_width-1: # If x < image width
                            pos1_value = img[y, x + 1]  # px value to the right
                            #print("Searching east...")
                            if pos1_value != 0 and pos1_coordinates not in self.white_pixels:
                                #print("White pixel detected at position 1: (y, x)", pos1_coordinates)
                                self.output_list[pos1_coordinates[0]][pos1_coordinates[1]] = self.blob_number
                                self.queue.append(pos1_coordinates)
                                self.white_pixels.append(pos1_coordinates)
                            elif pos1_coordinates in self.white_pixels:
                                #print("White pixel have already been saved.")
                                pass
                            elif pos1_value == 0 and pos1_coordinates not in self.black_pixels:
                                #print("A black pixel were found.")
                                self.black_pixels.append(pos1_coordinates)
                        else:
                            #print("East is out of bounds.")
                            pass

                        if current_pos[0] < self.img_height - 1:
                            pos2_value = img[y + 1, x]  # px value below
                            #print("Searching south...")
                            if pos2_value != 0 and pos2_coordinates not in self.white_pixels:
                                #print("White pixel detected at position 2: (y, x)", pos2_coordinates)
                                self.output_list[pos2_coordinates[0]][pos2_coordinates[1]] = self.blob_number
                                self.queue.append(pos2_coordinates)
                                self.white_pixels.append(pos2_coordinates)
                            elif pos2_coordinates in self.white_pixels:
                                #print("White pixel have already been saved.")
                                pass
                            elif pos2_value == 0 and pos2_coordinates not in self.black_pixels:
                                #print("A black pixel were found.")
                                self.black_pixels.append(pos2_coordinates)
                        else:
                            #print("South is out of bounds.")
                            pass

                        if current_pos[1] > 0:
                            pos3_value = img[y, x - 1]  # px value to the left
                            #print("Searching west...")
                            # If not black and not already found:
                            if pos3_value != 0 and pos3_coordinates not in self.white_pixels:
                                #print("White pixel detected at position 3: (y, x)", pos3_coordinates)
                                self.output_list[pos2_coordinates[0]][pos2_coordinates[1]] = self.blob_number
                                self.queue.append(pos3_coordinates)
                                self.white_pixels.append(pos3_coordinates)
                            elif pos3_coordinates in self.white_pixels:
                                #print("White pixel have already been saved.")
                                pass
                            elif pos3_value == 0 and pos3_coordinates not in self.black_pixels:
                                #print("A black pixel were found.")
                                self.black_pixels.append(pos3_coordinates)
                        else:
                            #print("West is out of bounds.")
                            pass

                        if current_pos[0] > 0:
                            pos4_value = img[y - 1, x]  # px value above
                            #print("Searching north...")
                            if pos4_value != 0 and pos4_coordinates not in self.white_pixels:
                                #print("White pixel detected at position 4: (y, x)", pos4_coordinates)
                                self.output_list[y-1][x] = self.blob_number
                                self.queue.append(pos4_coordinates)
                                self.white_pixels.append(pos4_coordinates)
                            elif pos4_coordinates in self.white_pixels:
                                #print("White pixel have already been saved.")
                                pass
                            elif pos4_value == 0 and pos4_coordinates not in self.black_pixels:
                                #print("A black pixel were found.")
                                self.black_pixels.append(pos4_coordinates)
                        else:
                            #print("North is out of bounds.")
                            pass

                    elif current_value == 0 and current_pos not in self.black_pixels:
                        self.black_pixels.append(current_pos)


                # If que is not empty, continue searching for pixels in the current blob.
                for i in range(0, len(self.queue)):
                    current_pos = self.queue[0]
                    #current_value = img[self.queue[0]]

                    pos1_coordinates = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                    pos2_coordinates = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                    pos3_coordinates = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                    pos4_coordinates = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                    #print("\nQueue:", self.queue)
                    #print("Searching at index in queue", self.queue[0], " = Current position:", current_pos)


                    # Grass-fire search
                    # If x < image width
                    if current_pos[1] < self.img_width-1:
                        pos1_value = img[pos1_coordinates[0], pos1_coordinates[1]]  # px value to the right
                        #print("Searching east...")
                        if pos1_value != 0 and pos1_coordinates not in self.white_pixels:
                            #print("White pixel detected at position 1: (y, x)", pos1_coordinates)
                            self.output_list[pos1_coordinates[0]][pos1_coordinates[1]] = self.blob_number
                            self.queue.append(pos1_coordinates)
                            self.white_pixels.append(pos1_coordinates)
                        elif pos1_coordinates in self.white_pixels:
                            #print("White pixel have already been saved.")
                            pass
                        elif pos1_value == 0 and pos1_coordinates not in self.black_pixels:
                            #print("A black pixel were found.")
                            self.black_pixels.append(pos1_coordinates)
                    else:
                        #print("East is out of bounds.")
                        pass

                    if current_pos[0] < self.img_height-1:
                        pos2_value = img[pos2_coordinates[0], pos2_coordinates[1]]  # px value below
                        #print("Searching south...")
                        if pos2_value != 0 and pos2_coordinates not in self.white_pixels:
                            #print("White pixel detected at position 2: (y, x)", pos2_coordinates)
                            self.output_list[pos2_coordinates[0]][pos2_coordinates[1]] = self.blob_number
                            self.queue.append(pos2_coordinates)
                            self.white_pixels.append(pos2_coordinates)
                        elif pos2_coordinates in self.white_pixels:
                            #print("White pixel have already been saved.")
                            pass
                        elif pos2_value == 0 and pos2_coordinates not in self.black_pixels:
                            #print("A black pixel were found.")
                            self.black_pixels.append(pos2_coordinates)
                    else:
                        #print("South is out of bounds.")
                        pass

                    if current_pos[1] > 0:
                        pos3_value = img[pos3_coordinates[0], pos3_coordinates[1]]  # px value to the left
                        #print("Searching west...")
                        # If not black and not already found:
                        if pos3_value != 0 and pos3_coordinates not in self.white_pixels:
                            #print("White pixel detected at position 3: (y, x)", pos3_coordinates)
                            self.output_list[pos3_coordinates[0]][pos3_coordinates[1]] = self.blob_number
                            self.queue.append(pos3_coordinates)
                            self.white_pixels.append(pos3_coordinates)
                        elif pos3_coordinates in self.white_pixels:
                            #print("White pixel have already been saved.")
                            pass
                        elif pos3_value == 0 and pos3_coordinates not in self.black_pixels:
                            #print("A black pixel were found.")
                            self.black_pixels.append(pos3_coordinates)
                    else:
                        #print("West is out of bounds.")
                        pass

                    if current_pos[0] > 0:
                        pos4_value = img[pos4_coordinates[0], pos4_coordinates[1]]  # px value above
                        #print("Searching north...")
                        if pos4_value != 0 and pos4_coordinates not in self.white_pixels:
                            #print("White pixel detected at position 4: (y, x)", pos4_coordinates)
                            self.output_list[pos4_coordinates[0]][pos4_coordinates[1]] = self.blob_number
                            self.queue.append(pos4_coordinates)
                            self.white_pixels.append(pos4_coordinates)
                        elif pos4_coordinates in self.white_pixels:
                            #print("White pixel have already been saved.")
                            pass
                        elif pos4_value == 0 and pos4_coordinates not in self.black_pixels:
                            #print("A black pixel were found.")
                            self.black_pixels.append(pos4_coordinates)
                    else:
                        #print("North is out of bounds.")
                        pass

                    self.queue.remove(self.queue[0])

        #print("White pixels:", self.white_pixels)
        #print("Number of white pixels:", len(self.white_pixels))
        #print("Black pixels:", self.black_pixels)
        #print("Number of black pixels:", len(self.black_pixels))

        print("Grass-fire is done.")
        #print("Output list:\n", self.output_list)

        return self.output_list


    def greatestBlob(self):
        greatest_blob = 0

        for j in range(1, self.blob_number+1):
            blob_size = sum(i.count(j) for i in self.output_list) # counts number of each element in list. i = index, j = element.
            #print(blob_size, j)
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

        #print("list:\n", self.output_list)
        # A list containing only 0's and 1's is returned.
        return self.output_list


    # recolors the image based on the binary output list, such that only the greatest blob remains.
    def outputImage(self):
        # img[y, x] = pixel value, 0 or 255
        # self.output_list[y][x] = value in output list, 0 or 1

        #searches through the image image.
        for y in range(0, self.img_height):
            for x in range(0, self.img_width):
                # if the pixel value is not 0 (black) and the value in the output list is black, change the pixel value
                # in the image to black.
                if self.img[y, x] != 0 and self.output_list[y][x] == 0:
                    self.img[y, x] = 0
        return self.img

        #print("image yes\n", self.img)


    def startGrassFire(self):
        self.outputSize()
        print('Step one complete')
        self.grassFire(self.img)
        print('Step two complete')
        self.greatestBlob()
        print('Step three complete')
        self.outputList()
        print('Step four complete')
        self.outputImage()
        print('Step five complete')


        return self.img
