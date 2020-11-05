import cv2
import numpy as np
from HandTracking.CameraHandler import *
from HandTracking.Modules.SobelEdge import *
from HandTracking.GrassFire import *
from HandTracking.Thresholding import *


if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    #
    # cameraHandler = CameraHandler(cap)
    # cameraHandler.grabFrame()

    th = Thresholding()

    frame = cv2.imread('./Pictures/Green_Hand_Four.png')

    binary = th.binarize(frame)


    # gf = GrassFire(binary)
    cv2.imshow('b', binary)
    # print(binary)
    # gf.startGrassFire()
    #


    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
