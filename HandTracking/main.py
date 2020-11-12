import cv2
import numpy as np
from HandTracking.CameraHandler import *
from HandTracking.Modules.SobelEdge import *
from HandTracking.GrassFire import *
from HandTracking.Thresholding import *
from HandTracking.HistogramProjection import *
from HandTracking.Compactness import *
from HandTracking.AspectRatio import *


if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    #
    # cameraHandler = CameraHandler(cap)
    # cameraHandler.grabFrame()

    th = Thresholding()

    frame = cv2.imread('./PicsEval/A1.jpg', cv2.COLOR_BGR2HSV)

    binary = th.binarize(frame)
    cv2.imshow('yes', binary)
    cv2.waitKey(0)

    gr = GrassFire(img=binary)
    grass = gr.startGrassFire()

    # pic = grass.startGrassFire()
    # # print('pic', pic)
    # # #
    # #
    # gf = GrassFire(binary)
    cv2.imshow('yes', grass)
    # cv2.imshow('pic', pic)
    # # cv2.imwrite('C6B.jpg', pic)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
