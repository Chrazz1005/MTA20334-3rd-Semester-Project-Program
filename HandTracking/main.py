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
from HandTracking.CompoundOperations import *
from multiprocessing import Process

if __name__ == '__main__':
    # cap = cv2.VideoCapture(0)
    #
    # cameraHandler = CameraHandler(cap)
    # cameraHandler.grabFrame()


    #frame = cv2.imread('./PicsEval/C4.jpg', cv2.COLOR_BGR2HSV)
    vid = cv2.VideoCapture(0) # 0 = main intern


    frameCount = 0
    while (True):


        # Capture the video frame
        # by frame

        #frame = cv2.imread('./DataSetPics/frame2.jpg')

        ret, frame = vid.read()
        cv2.imshow('yes', frame)
        cv2.imwrite("./DataSetPics/frame%d.jpg" % frameCount, frame)
        th = Thresholding()
        binary = th.binarize(frame)

        #EROSION! :::::
        # cv2.imshow("no", binary)
        # cv2.waitKey(0)
        # cb = CompoundOperations(binary)
        # CompoundOperations.erode(cb)
        # fuck = CompoundOperations.get_image(cb)
        # cv2.imshow('yes', fuck)
        # cv2.waitKey(0)

        gr = GrassFire(binary)
        grass = gr.startGrassFire()

        if cv2.countNonZero(grass) == 0:
            # If all values are zero, the image is black.
            print("No BLOBs were found.")
        else:
            # If the image is not completely black, find features of BLOB:
            bb = BoundingBox(grass)
            croppedImage = bb.cropImage()


            # cv2.imshow("img", croppedImage)
            # cv2.waitKey(0)

            ap = AspectRatio(croppedImage)
            cp = Compactness(croppedImage)
            ph = ProjectionHistogram(croppedImage)

            cv2.imwrite("./DataSetPics/binary%d.jpg" % frameCount, grass)
            ed = EuclideanDistance()
            ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                        ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())
            # [aspectRatio, compactness, heightRelation, verticalRatio, horizontalRatio, localMaximum]

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice

        frameCount += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()

    # cv2.imshow('yes',grass)
    # cv2.waitKey(0)
    cv2.destroyAllWindows()

    # When everything done, release the capture
    # cap.release()
    # cv2.destroyAllWindows()
