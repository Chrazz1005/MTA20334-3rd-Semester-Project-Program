import cv2
import numpy as np
from HandTracking.CameraHandler import *

cap = cv2.VideoCapture(0)

cameraHandler = CameraHandler(cap)


cameraHandler.grabFrame()



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
