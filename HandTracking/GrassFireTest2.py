import numpy as np
import time



class GrassFireTest2:

    def __init__(self, img):
        self.img = img
        self.img_height = self.img.shape[0]  # 0 = height
        self.img_width = self.img.shape[1]  # 1 = width
        self.binary_array = np.zeros(img.shape, dtype=np.uint8) #Zero Array
        print(self.binary_array.shape)
        self.numbers = 0


    def grassFire(self):
        outputSizeTime = time.time()
        img = self.img
        array = self.binary_array
        label = 1 #Label for blobs.

        for y in range(0, self.img_height):
            for x in range(0, self.img_width):
                # if img[y, x] == 0:
                #     continue

                if img[y, x] == 255:

                    array[y,x] = label

                    #check north and west pixel
                    if img[y, x - 1] == 255 and img[y -1, x] == 255:

                        #Multiple pixels match and are all the same label
                        if array[y, x - 1] == array[y -1, x]:
                            array[y,x] = array[y, x-1]

                        # Multiple pixels match, but are different labels. They're therefore all equivalent.
                        elif array[y, x -1] != array[y -1, x]:

                            #Python Magiiiiic
                            # assigning all equivalent regions the same value.
                            if array[y, x -1] > array[y -1, x]:
                                array[array == array[y,x -1]] = array[y -1, x]

                            elif array[y, x -1] < array[y -1, x]:
                                array[array == array[y -1, x]] = array[y, x -1]

                            else:
                                print("Error in python magic")


                    #No pixels around this. increment region counter.
                    elif img[y, x - 1] == 0 and img[y -1, x] == 0:
                        array[y,x] = label
                        label += 1



                    #one pixel borders
                    elif img[y, x - 1] == 255 and img[y - 1, x] == 0:
                        array[y,x] = array[y, x-1]

                    elif img[y, x - 1] == 0 and img[y - 1, x] == 255:
                        array[y,x] = array[y -1, x]

                    else:
                        print("Error in grassfire.")

        self.numbers = label
        self.binary_array = array
        print("GrassFire: outputSize time: %s" % round((time.time() - outputSizeTime), 2), "seconds")



    def greatestBlob(self):
        greatestBlobTime = time.time()
        greatest_blob = 0
        arr = self.binary_array
        blob_number_greatest = 0


        # Finds the greatest blob
        for j in range(1, self.numbers + 1):
            blob_size = len(arr[arr == j]) # == j, takes lenght.
            if blob_size > greatest_blob: #er lengten større end den største blob?
                greatest_blob = blob_size # Størrelsen af blobben
                blob_number_greatest = j # Nummeret af blobben.

        # When the value is not the number of the greatest blob, change to zero.
        arr[arr != blob_number_greatest] = 0
        # Change the number to 1, such that the array consists of 0's and 1's, where 1 is the greatest blob.
        arr[arr == blob_number_greatest] = 255
        #arr = (arr / blob_number_greatest)*255

        print("GrassFire: greatestBlob time: %s" % round((time.time() - greatestBlobTime), 2), "seconds")
        return arr
















