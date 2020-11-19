import numpy as np
import cv2


# Hardcoding a cross-kernel 3x3 (1 in top, 3 in middle, 1 at bottom.)

def erosion(img, y, x):
    if img[y, x].all() == 0: #.any() because we have 3 channels that are 0's.
        return 0
    img_Height = img.shape[0]
    img_Width = img.shape[1]
    position = img[y,x] # y,x
    if [position[0], position[1] - 1] == 1 or x>=0: # y,x-1
        if [position[0], position[1] + 1] == 1 or x<=img_Width: # y,x+1
            if [position[0] + 1, position[1]] == 1 or x<=img_Height: # y+1,x
                if [position[0] - 1, position[1]] == 1 or x>=0: # y-1,x
                    return 255
    return 0


#Test-Picture:
test = cv2.imread("binaryC.png")


#Creating an array with 0's in the size of the picture.
dilutedArray = np.zeros(test.shape,dtype=np.uint8)

#The loop that goes through the picture:
for x in range(test.shape[1]-1):
    for y in range(test.shape[0]-1):
        dilutedArray[y,x] = erosion(test, y, x)


#For "testing" to see how well it works:
cv2.imshow("yay", dilutedArray)
cv2.waitKey(0)
print(test[0,0])
