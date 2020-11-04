import cv2
import numpy as np
from HandTracking.CameraHandler import *
from HandTracking.Modules.SobelEdge import *
from HandTracking.GrassFire import *
from HandTracking.Thresholding import *

cap = cv2.VideoCapture(0)

cameraHandler = CameraHandler(cap)
cameraHandler.grabFrame()
gf = GrassFire()
th = Thresholding()


if __name__ == '__main__':

    frame = cv2.imread('frame.jpg', cv2.IMREAD_COLOR)

    th.binarize(frame)
    gf.startGrassFire(th.binarize(frame))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
