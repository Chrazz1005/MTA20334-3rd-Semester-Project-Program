from MTA20334_Version_2_Slow.AspectRatio import *
from MTA20334_Version_2_Slow.BoundingBox import *
from MTA20334_Version_2_Slow.Compactness import *
from MTA20334_Version_2_Slow.EuclideanDistance import *
from MTA20334_Version_2_Slow.ProjectionHistograms import *
from MTA20334_Version_2_Slow.Thresholding import *
from MTA20334_Version_2_Slow.GrassFire import *


def displayWebcam(mirror=False):
    framecount = 0
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

        if cv2.countNonZero(t.binarize(img)) < 100:
            # If all values are zero, the image is black.
            print("No BLOBs were found.")
        else:

            gr = GrassFire(t.binarize(img))
            grassArray = gr.startGrassFire()

            bb = BoundingBox(grassArray)
            croppedImage = bb.cropImage()

            ap = AspectRatio(croppedImage)
            cp = Compactness(croppedImage)

            ph = ProjectionHistogram(croppedImage)

            cv2.imwrite("./Datasetslow/grass%d.jpg" % framecount, grassArray)
            cv2.imwrite("./Datasetslow/bb%d.jpg" % framecount, croppedImage)
            ed = EuclideanDistance()
            ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                        ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())

            framecount += 1

    cv2.destroyAllWindows()


def main():
    displayWebcam(mirror=True)


if __name__ == '__main__':
    main()
