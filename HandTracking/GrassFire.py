import cv2


class GrassFire:

    img = cv2.imread("binaryHand.png", 0)  # 0 = grayscale
    img_height = img.shape[0]  # Shape: 0 = height, 1 = width, 2 = color
    img_width = img.shape[1]

    white = 255
    gray = 150
    black = 0

    blob_number = 1

    queue = []
    white_pixels = []

    def grassFire(self, img):

        for y in range(0, self.img_height):
            for x in range(0, self.img_width):

                current_pos = [y, x]
                pos1_coordinates = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                pos2_coordinates = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                pos3_coordinates = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                pos4_coordinates = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                current_value = img[y, x]

                # If queue is empty, search for blobs.
                if len(self.queue) == 0:

                    # If a white pixel is found, start grass-fire search
                    if current_value == self.white and current_pos not in self.white_pixels:
                        self.white_pixels.append(current_pos)
                        print("\nFound new BLOB at:", current_pos)

                        # Grass-fire search
                        # If x < image width
                        if current_pos[1] < self.img_width-1:
                            pos1_value = img[y, x + 1]  # px value to the right
                            print("Searching east...")
                            if pos1_value != 0 and pos1_coordinates not in self.white_pixels:
                                print("White pixel detected at position 1: (y, x)", pos1_coordinates)
                                self.queue.append(pos1_coordinates)
                                self.white_pixels.append(pos1_coordinates)
                            elif pos1_coordinates in self.white_pixels:
                                print("White pixel have already been saved.")
                            else:
                                print("No white pixels were found.")
                        else:
                            print("East is out of bounds.")

                        if current_pos[0] < self.img_height-1:
                            pos2_value = img[y + 1, x]  # px value below
                            print("Searching south...")
                            if pos2_value != 0 and pos2_coordinates not in self.white_pixels:
                                print("White pixel detected at position 2: (y, x)", pos2_coordinates)
                                self.queue.append(pos2_coordinates)
                                self.white_pixels.append(pos2_coordinates)
                            elif pos2_coordinates in self.white_pixels:
                                print("White pixel have already been saved.")
                            else:
                                print("No white pixels were found.")
                        else:
                            print("South is out of bounds.")

                        if current_pos[1] > 0:
                            pos3_value = img[y, x - 1]  # px value to the left
                            print("Searching west...")
                            # If not black and not already found:
                            if pos3_value != 0 and pos3_coordinates not in self.white_pixels:
                                print("White pixel detected at position 3: (y, x)", pos3_coordinates)
                                self.queue.append(pos3_coordinates)
                                self.white_pixels.append(pos3_coordinates)
                            elif pos3_coordinates in self.white_pixels:
                                print("White pixel have already been saved.")
                            else:
                                print("No white pixels were found.")
                        else:
                            print("West is out of bounds.")

                        if current_pos[0] > 0:
                            pos4_value = img[y - 1, x]  # px value above
                            print("Searching north...")
                            if pos4_value != 0 and pos4_coordinates not in self.white_pixels:
                                print("White pixel detected at position 4: (y, x)", pos4_coordinates)
                                self.queue.append(pos4_coordinates)
                                self.white_pixels.append(pos4_coordinates)
                            elif pos4_coordinates in self.white_pixels:
                                print("White pixel have already been saved.")
                            else:
                                print("No white pixels were found.")
                        else:
                            print("North is out of bounds.")

                # If que is not empty, continue searching for pixels in the current blob.
                for i in range(0, len(self.queue)):
                    current_pos = self.queue[0]
                    pos1_coordinates = [current_pos[0], current_pos[1] + 1]  # [y, x + 1]
                    pos2_coordinates = [current_pos[0] + 1, current_pos[1]]  # [y + 1, x]
                    pos3_coordinates = [current_pos[0], current_pos[1] - 1]  # [y, x - 1]
                    pos4_coordinates = [current_pos[0] - 1, current_pos[1]]  # [y - 1, x]

                    current_value = img[current_pos]


                    print("\nQueue:", self.queue)
                    print("Searching at index in queue", self.queue[0], " = Current position:", current_pos)
                    self.queue.remove(self.queue[0])

                    # Grass-fire search
                    # If x < image width
                    if current_pos[1] < self.img_width-1:
                        pos1_value = img[pos1_coordinates[0], pos1_coordinates[1]]  # px value to the right
                        print("Searching east...")
                        if pos1_value != 0 and pos1_coordinates not in self.white_pixels:
                            print("White pixel detected at position 1: (y, x)", pos1_coordinates)
                            self.queue.append(pos1_coordinates)
                            self.white_pixels.append(pos1_coordinates)
                        elif pos1_coordinates in self.white_pixels:
                            print("White pixel have already been saved.")
                        else:
                            print("No white pixels were found.")
                    else:
                        print("East is out of bounds.")

                    if current_pos[0] < self.img_height-1:
                        pos2_value = img[pos2_coordinates[0], pos2_coordinates[1]]  # px value below
                        print("Searching south...")
                        if pos2_value != 0 and pos2_coordinates not in self.white_pixels:
                            print("White pixel detected at position 2: (y, x)", pos2_coordinates)
                            self.queue.append(pos2_coordinates)
                            self.white_pixels.append(pos2_coordinates)
                        elif pos2_coordinates in self.white_pixels:
                            print("White pixel have already been saved.")
                        else:
                            print("No white pixels were found.")
                    else:
                        print("South is out of bounds.")

                    if current_pos[1] > 0:
                        pos3_value = img[pos3_coordinates[0], pos3_coordinates[1]]  # px value to the left
                        print("Searching west...")
                        # If not black and not already found:
                        if pos3_value != 0 and pos3_coordinates not in self.white_pixels:
                            print("White pixel detected at position 3: (y, x)", pos3_coordinates)
                            self.queue.append(pos3_coordinates)
                            self.white_pixels.append(pos3_coordinates)
                        elif pos3_coordinates in self.white_pixels:
                            print("White pixel have already been saved.")
                        else:
                            print("No white pixels were found.")
                    else:
                        print("West is out of bounds.")

                    if current_pos[0] > 0:
                        pos4_value = img[pos4_coordinates[0], pos4_coordinates[1]]  # px value above
                        print("Searching north...")
                        if pos4_value != 0 and pos4_coordinates not in self.white_pixels:
                            print("White pixel detected at position 4: (y, x)", pos4_coordinates)
                            self.queue.append(pos4_coordinates)
                            self.white_pixels.append(pos4_coordinates)
                        elif pos4_coordinates in self.white_pixels:
                            print("White pixel have already been saved.")
                        else:
                            print("No white pixels were found.")
                    else:
                        print("North is out of bounds.")

        print("Grass-fire is done.")
        print("White pixels:", self.white_pixels)
        print("Number of white pixels:", len(self.white_pixels))
        cv2.imshow("Image", img)
        cv2.waitKey(0)


