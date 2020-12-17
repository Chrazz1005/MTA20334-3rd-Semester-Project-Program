from MTA20334_Version_2_Slow.AspectRatio import *
from MTA20334_Version_2_Slow.BoundingBox import *
from MTA20334_Version_2_Slow.Compactness import *
from MTA20334_Version_2_Slow.DataCollection import *
from MTA20334_Version_2_Slow.GrassFire import *
from MTA20334_Version_2_Slow.ProjectionHistograms import *
from MTA20334_Version_2_Slow.Thresholding import *


def displayWebcam(mirror=False):
    iterations = 0
    t = Thresholding()
    cam = cv2.VideoCapture(0)
    frameCount = 0
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

            cv2.imwrite("./Datasetslow/binary%d.jpg" % frameCount, croppedImage)
            ed = EuclideanDistance()
            key = ed.distance(ap.calculateAspectRatio(), cp.calculateCompactness(), ph.checkMaxHeightRelation(),
                              ph.checkVertSizeRatio(), ph.checkHoriSizeRatio(), ph.checkMaximumRelations())

            asp = ap.calculateAspectRatio()
            cmp = cp.calculateCompactness()
            mhr = ph.checkMaxHeightRelation()
            mr = ph.checkMaximumRelations()
            vsr = ph.checkVertSizeRatio()
            hsr = ph.checkHoriSizeRatio()

            dc = DataCollection()
            dc.content.append(key)
            dc.aspList.append(asp)
            dc.cmpList.append(cmp)
            dc.mhrList.append(mhr)
            dc.mrList.append(mr)
            dc.vsrList.append(vsr)
            dc.hsrList.append(hsr)
            dc.createColumns()

            if iterations >= 29:
                dc.startDataCollection()
                print("Document was Saved! FUCK YES!!")

            iterations += 1
            frameCount += 1

            cv2.imshow("Binarized Webcam", t.binarize(img))
            cv2.waitKey(0)

    cv2.destroyAllWindows()


def main():
    displayWebcam(mirror=True)


if __name__ == '__main__':
    main()
