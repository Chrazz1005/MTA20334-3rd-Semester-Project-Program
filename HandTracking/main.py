import cv2
import numpy as np
from HandTracking.CameraHandler import *
from HandTracking.Modules.SobelEdge import *

cap = cv2.VideoCapture(0)
#
# cameraHandler = CameraHandler(cap)
# frames = cameraHandler.grabFrame()

frame = cv2.imread('a.jpg', cv2.IMREAD_COLOR)
sobelEdge = SobelEdge(frame)
edges = sobelEdge.detectionLoop()


cv2.imshow('edge', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
