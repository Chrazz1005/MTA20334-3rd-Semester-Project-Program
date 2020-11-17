import cv2
import numpy as np
from HandTracking.CameraHandler import *
from HandTracking.Modules.SobelEdge import *
from HandTracking.GrassFire import *
from HandTracking.Thresholding import *
from HandTracking.HistogramProjection import *
from HandTracking.Compactness import *
from HandTracking.AspectRatio import *
from HandTracking.ProjectionHistograms import *
from HandTracking.EuclideanDistance import *


if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    #
    # cameraHandler = CameraHandler(cap)
    # cameraHandler.grabFrame()

    th = Thresholding()

    frame = cv2.imread('./PicsEval/A1.jpg', cv2.COLOR_BGR2HSV)

    binary = th.binarize(frame)
    #cv2.imshow('yes', binary)
    #cv2.waitKey(0)

    gr = GrassFire(binary)
    grass = gr.startGrassFire()

    cp = Compactness(binary)
    #cp.printResults()
    ap = AspectRatio(binary)
    print(ap.compareAspectRatio())

    ph = ProjectionHistogram(binary)

    ed = EuclideanDistance()
    ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(), ph.checkVertSizeRatio(),
                ph.checkHoriSizeRatio(), ph.checkMaximumRelations())
    # [aspectRatio, compactness, heightRelation, verticalRatio, horizontalRatio, localMaximum]

    cv2.imshow('yes', grass)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
