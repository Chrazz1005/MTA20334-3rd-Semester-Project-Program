from HandTracking.AspectRatio import *
from HandTracking.Compactness import *
from HandTracking.EuclideanDistance import *
from HandTracking.ProjectionHistograms import *
from HandTracking.Thresholding import *
from HandTracking.GrassFire import *


def displayWebcam(mirror=False):
    t = Thresholding()
    cam = cv2.VideoCapture(0)
    while True:
        ret, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        cv2.imshow("Webcam", img)
        cv2.imshow("Binarized Webcam", t.binarize(img))
        if cv2.waitKey(1) == 27:
            break  # esc to quit

        if cv2.countNonZero(t.binarize(img)) == 0:
            # If all values are zero, the image is black.
            print("No BLOBs were found.")
        else:

            gr = GrassFire(t.binarize(img))
            grassArr = gr.startGrassFire()

            bb = BoundingBox(grassArr)
            achoo = bb.cropImage()

            ap = AspectRatio(achoo)
            cp = Compactness(achoo)

            ph = ProjectionHistogram(achoo)

            # cv2.imwrite("./DataSetPics/binary%d.jpg" % frameCount, grass)
            ed = EuclideanDistance()
            ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                        ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())

    cv2.destroyAllWindows()


def main():
    displayWebcam(mirror=True)


if __name__ == '__main__':
    main()
