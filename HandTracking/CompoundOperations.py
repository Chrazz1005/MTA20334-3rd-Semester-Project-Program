import numpy as np
import cv2


class CompoundOperations:
    def __init__(self, img):
        self.img = img
        dilutedArray = np.zeros(img.shape, dtype=np.uint8)
        self.dilutedArray = dilutedArray

        # if method is dilution:
        #     self.method = dilution(img)

    def erode(self):
        img = self.img
        dilutedArray = self.dilutedArray
        print(dilutedArray.shape)
        for x in range(img.shape[1] - 1):
            #print("x in range", x)
            for y in range(img.shape[0] - 1):
                print(y)
                dilutedArray[y, x] = erosion(img, y, x)
        return dilutedArray

    def get_image(self):
        return self.dilutedArray




# Hardcoding a cross-kernel 3x3 (1 in top, 3 in middle, 1 at bottom.)

def erosion(img, y, x):
    if img[y, x].all() == 0: #.any() because we have 3 channels that are 0's.
        return 0
    # img_Height = img.shape[0]
    # img_Width = img.shape[1]
    # img[y,x] # y,x
    if img[y, x-1] == 255: # y,x-1
        if img[y, x + 1] == 255: # y,x+1
            if img[y + 1, x] == 255: # y+1,x
                if img[y - 1, x] == 255: # y-1,x
                    return 255
    return 0

        #hvis det skal være en firkant kernel, tilføj den her til if statement-hellet. ^
    # if img[y - 1, x - 1] == 255:
    #     if img[y - 1, x + 1] == 255:
    #         if img[y + 1, x + 1] == 255:
    #             if img[y + 1, x - 1] == 255:
    #                 return 255

    #MÅSKE ET PROBLEM, hvis listen er for lang altså når den minuser 1 og + 1 hvis den går ud af billedet, men ved det ikke endnu.

    # if [position[0], position[1] - 1] == 255 or x>=0: # y,x-1
    #     # print("true1")
    #     if [position[0], position[1] + 1] == 255 or x<=img_Width: # y,x+1
    #         if [position[0] + 1, position[1]] == 255 or x<=img_Height: # y+1,x
    #             if [position[0] - 1, position[1]] == 255 or x>=0: # y-1,x
    #                 return 255
    # return 0


#Test-Picture:
# arraytest = np.array([[
# testarray = np.array([  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [  0,   0,   0], [255, 255, 255],
#                      [255, 255, 255], [255, 255, 255], [255, 255, 255],
#  [  0   0   0])
#
# test = cv2.imread("binaryC.png")
# print(test[200])


#
# #Creating an array with 0's in the size of the picture.
# dilutedArray = np.zeros(test.shape,dtype=np.uint8)

#The loop that goes through the picture:
# for x in range(test.shape[1]-1):
#     for y in range(test.shape[0]-1):
#         dilutedArray[y,x] = erosion(test, y, x)

# CV = CompoundOperations(arraytest)
# for x in range(10):
#     CompoundOperations.erode(CV)
# Fuck = CompoundOperations.get_image(CV)
#For "testing" to see how well it works:


# cv2.imshow("yay",Fuck)
# cv2.waitKey(0)
# print(test[0,0])
