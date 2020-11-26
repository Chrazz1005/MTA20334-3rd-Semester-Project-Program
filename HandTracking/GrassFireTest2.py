import numpy as np


class GrassFireTest2:

    def __init__(self, img):
        self.img = img
        self.img_height = self.img.shape[0]  # 0 = height
        self.img_width = self.img.shape[1]  # 1 = width
        self.binary_array = np.zeros(img.shape, dtype=np.uint8) #Zero Array


    def grassFire(self):
        img = self.img
        array = self.binary_array
        i = 1 #Label for blobs.

        for y in range(0, self.img_height):
            for x in range(0, self.img_width):
                if img[y, x] == 0:
                    array[y, x] = 0
                if img[y, x] == 255:
                    array[y, x] = i

                    #Is the pixel above our pixel white?
                    if img[y - 1, x] == 255:
                        if array[y- 1, x] <= array[y, x]:
                            array[y, x] = array[y - 1, x]
                        array[y- 1, x] = array[y,x]

                    #Is the pixel behind our pixel white?
                    if img[y , x - 1] == 255:
                        if array[y, x - 1] <= array[y, x]:
                            array[y, x] = array[y, x - 1]
                    i = array[y,x] + 1
        return array


    def grassWater(self):
        array = self.binary_array

        for y in range(self.img_height, 0):
            for x in range(self.img_width, 0):
                if array[y, x] == 0:
                    pass
                if array[y, x] != 0:

                    if array[y, x + 1] != 0 or array[y + 1, x] != 0:
                        if 0 != array[y + 1, x] >= array[y, x + 1] != 0:
                            array[y, x] = array[y, x + 1]
                        else:
                            array[y, x] = array[y + 1, x]
        return array


