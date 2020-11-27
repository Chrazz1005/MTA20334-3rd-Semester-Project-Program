# from sklearn import preprocessing
import numpy as np


class EuclideanDistance:
    debug = False

    # The intervals that determine which hand sign has been detected.
    aspectRatio_A_min = 2.04
    aspectRatio_A_max = 2.27
    aspectRatio_B_min = 1.42
    aspectRatio_B_max = 1.50
    aspectRatio_C_min = 0.90
    aspectRatio_C_max = 1.06

    ar_Astd = 0.0656295
    ar_Aavg = 0.00108783
    ar_Amax = ar_Aavg + ar_Astd
    ar_Amin = ar_Aavg - ar_Astd

    ar_Bstd = 0.04313208
    ar_Bavg = 0.001211328
    ar_Bmin = ar_Bavg - ar_Bstd
    ar_Bmax = ar_Bavg + ar_Bstd

    ar_Cstd = 0.04622898
    ar_Cavg = 0.001144468
    ar_Cmin = ar_Cavg - ar_Cstd
    ar_Cmax = ar_Cavg + ar_Cstd

    compactness_A_min = 73
    compactness_A_max = 81
    compactness_B_min = 80
    compactness_B_max = 83
    compactness_C_min = 46
    compactness_C_max = 48

    c_Astd = 0.00404755
    c_Aavg = 0.0629384
    c_Amax = c_Aavg + c_Astd
    c_Amin = c_Aavg - c_Astd

    c_Bstd = 0.002937374
    c_Bavg = 0.04212978
    c_Bmin = c_Bavg - c_Bstd
    c_Bmax = c_Bavg + c_Bstd

    c_Cstd = 0.006012833
    c_Cavg = 0.045000879
    c_Cmin = c_Cavg - c_Cstd
    c_Cmax = c_Cavg + c_Cstd

    heightRelation_A_min = 0.60
    heightRelation_A_max = 0.80
    heightRelation_B_min = 0.35
    heightRelation_B_max = 0.60
    heightRelation_C_min = 1.10
    heightRelation_C_max = 1.40

    hr_Astd = 0.06596106
    hr_Aavg = 0.0007752173
    hr_Amax = hr_Aavg + hr_Astd
    hr_Amin = hr_Aavg - hr_Astd

    hr_Bstd = 0.04409414
    hr_Bavg = 0.0002984198
    hr_Bmin = hr_Bavg - hr_Bstd
    hr_Bmax = hr_Bavg + hr_Bstd

    hr_Cstd = 0.04664601
    hr_Cavg = 0.0007490136
    hr_Cmin = hr_Cavg - hr_Cstd
    hr_Cmax = hr_Cavg + hr_Cstd


    verticalRatio_A_min = 130
    verticalRatio_A_max = 160
    verticalRatio_B_min = 100
    verticalRatio_B_max = 130
    verticalRatio_C_min = 240
    verticalRatio_C_max = 260

    vertihr_Astd = 0.1351614
    vertihr_Aavg = 0.1885497
    vertihr_Amin = vertihr_Aavg - vertihr_Astd
    vertihr_Amax = vertihr_Aavg + vertihr_Astd

    vertihr_Bstd = 0.034432279
    vertihr_Bavg = 0.07424375
    vertihr_Bmin = vertihr_Bavg - vertihr_Bstd
    vertihr_Bmax = vertihr_Bavg + vertihr_Bstd

    vertihr_Cstd = 0.1305096
    vertihr_Cavg = 0.1649563
    vertihr_Cmin = vertihr_Cavg - vertihr_Cstd
    vertihr_Cmax = vertihr_Cavg + vertihr_Cstd

    horizontalRatio_A_min = 280
    horizontalRatio_A_max = 310
    horizontalRatio_B_min = 315
    horizontalRatio_B_max = 480
    horizontalRatio_C_min = 120
    horizontalRatio_C_max = 200

    horihr_Astd = 0.2167308
    horihr_Aavg = 0.2646185
    horihr_Amin = horihr_Aavg - horihr_Astd
    horihr_Amax = horihr_Aavg + horihr_Astd

    horihr_Bstd = 0.2768627
    horihr_Bavg = 0.30209657
    horihr_Bmin = horihr_Bavg - horihr_Bstd
    horihr_Bmax = horihr_Bavg + horihr_Bstd

    horihr_Cstd = 0.2321599
    horihr_Cavg = 0.25892256
    horihr_Cmin = horihr_Cavg - horihr_Cstd
    horihr_Cmax = horihr_Cavg + horihr_Cstd

    localMaximum_A_min = 0.8
    localMaximum_A_max = 1.1
    localMaximum_B_min = 1.1
    localMaximum_B_max = 1.5
    localMaximum_C_min = 1.8
    localMaximum_C_max = 2.2

    lmaxdiff_Astd = 0.06580879
    lmaxdiff_Aavg = 0.0009187231
    lmaxdiff_Amin = lmaxdiff_Aavg - lmaxdiff_Astd
    lmaxdiff_Amax = lmaxdiff_Aavg + lmaxdiff_Astd

    lmaxdiff_Bstd = 0.04359541
    lmaxdiff_Bavg = 0.0007715659
    lmaxdiff_Bmin = lmaxdiff_Bavg - lmaxdiff_Bstd
    lmaxdiff_Bmax = lmaxdiff_Bavg + lmaxdiff_Bstd

    lmaxdiff_Cstd = 0.04568783
    lmaxdiff_Cavg = 0.001658877
    lmaxdiff_Cmin = lmaxdiff_Cavg - lmaxdiff_Cstd
    lmaxdiff_Cmax = lmaxdiff_Cavg + lmaxdiff_Cstd


    A_min = np.array((aspectRatio_A_min, compactness_A_min, heightRelation_A_min, verticalRatio_A_min,
                      horizontalRatio_A_min, localMaximum_A_min))
    A_max = np.array((aspectRatio_A_max, compactness_A_max, heightRelation_A_max, verticalRatio_A_max,
                      horizontalRatio_A_max, localMaximum_A_max))
    B_min = np.array((aspectRatio_B_min, compactness_B_min, heightRelation_B_min, verticalRatio_B_min,
                      horizontalRatio_B_min, localMaximum_B_min))
    B_max = np.array((aspectRatio_B_max, compactness_B_max, heightRelation_B_max, verticalRatio_B_max,
                      horizontalRatio_B_max, localMaximum_B_max))
    C_min = np.array((aspectRatio_C_min, compactness_C_min, heightRelation_C_min, verticalRatio_C_min,
                      horizontalRatio_C_min, localMaximum_C_min))
    C_max = np.array((aspectRatio_C_max, compactness_C_max, heightRelation_C_max, verticalRatio_C_max,
                      horizontalRatio_C_max, localMaximum_C_max))

    def distance(self, aspectRatio, compactness, heightRelation, verticalRatio, horizontalRatio, localMaximum):
        inputCoordinates = np.array((aspectRatio, compactness, heightRelation, verticalRatio, horizontalRatio,
                                     localMaximum))

        data = np.array((self.A_min, self.A_max, self.B_min, self.B_max, self.C_min, self.C_max, inputCoordinates))
        data_normalized = data / np.linalg.norm(data)

        inputCoordinates = data_normalized[6]

        #print("Data:", data_normalized)
        #print("input coordinates:", inputCoordinates)

        # calculates the distance between the input coordinates and points
        distance_A_min = np.linalg.norm(data_normalized[0] - inputCoordinates)
        distance_A_max = np.linalg.norm(data_normalized[1] - inputCoordinates)
        distance_B_min = np.linalg.norm(data_normalized[2] - inputCoordinates)
        distance_B_max = np.linalg.norm(data_normalized[3] - inputCoordinates)
        distance_C_min = np.linalg.norm(data_normalized[4] - inputCoordinates)
        distance_C_max = np.linalg.norm(data_normalized[5] - inputCoordinates)

        handsigns = {
            "A": distance_A_min and distance_A_max,
            "B": distance_B_min and distance_B_max,
            "C": distance_C_min and distance_C_max
        }

        minDistance = min(handsigns.values())
        if self.debug:
            print("Distance to minimum A value:", round(distance_A_min, 2),
                  "\nDistance to maximum A value:", round(distance_A_max, 2),
                  "\nDistance to minimum B value:", round(distance_B_min, 2),
                  "\nDistance to maximum B value:", round(distance_B_max, 2),
                  "\nDistance to minimum C value:", round(distance_C_min, 2),
                  "\nDistance to maximum C value:", round(distance_C_max, 2), "\n")

        if self.debug:
            print("Min. distance:", minDistance)

        if minDistance < 0.1:
            for key, value in handsigns.items():
                if minDistance == value:
                    print("The gesture is:", key)
                    return key

        else:
            print("Neither A, B or C was detected.")
            return "NONE"
        #print('-----------------------------------------------')

