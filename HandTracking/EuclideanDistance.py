
import numpy as np


class EuclideanDistance:

    # The intervals that determine which hand sign has been detected.
    aspectRatio_A_min = 2.04
    aspectRatio_A_max = 2.27
    aspectRatio_B_min = 1.42
    aspectRatio_B_max = 1.50
    aspectRatio_C_min = 0.90
    aspectRatio_C_max = 1.06

    compactness_A_min = 73
    compactness_A_max = 81
    compactness_B_min = 80
    compactness_B_max = 83
    compactness_C_min = 46
    compactness_C_max = 48

    heightRelation_A_min = 0.60
    heightRelation_A_max = 0.80
    heightRelation_B_min = 0.35
    heightRelation_B_max = 0.60
    heightRelation_C_min = 1.10
    heightRelation_C_max = 1.40

    verticalRatio_A_min = 130
    verticalRatio_A_max = 160
    verticalRatio_B_min = 100
    verticalRatio_B_max = 130
    verticalRatio_C_min = 240
    verticalRatio_C_max = 260

    horizontalRatio_A_min = 280
    horizontalRatio_A_max = 310
    horizontalRatio_B_min = 315
    horizontalRatio_B_max = 480
    horizontalRatio_C_min = 120
    horizontalRatio_C_max = 200

    localMaximum_A_min = 0.8
    localMaximum_A_max = 1.1
    localMaximum_B_min = 1.1
    localMaximum_B_max = 1.5
    localMaximum_C_min = 1.8
    localMaximum_C_max = 2.2

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
        inputCoordinates = np.array([aspectRatio, compactness, heightRelation, verticalRatio, horizontalRatio,
                                     localMaximum])
        print("input coordinates:", inputCoordinates)

        # calculates the distance between the input coordinates and points
        distance_A_min = np.linalg.norm(self.A_min - inputCoordinates)
        distance_A_max = np.linalg.norm(self.A_max - inputCoordinates)
        distance_B_min = np.linalg.norm(self.B_min - inputCoordinates)
        distance_B_max = np.linalg.norm(self.B_max - inputCoordinates)
        distance_C_min = np.linalg.norm(self.C_min - inputCoordinates)
        distance_C_max = np.linalg.norm(self.C_max - inputCoordinates)

        handsigns = {
            "A": distance_A_min and distance_A_max,
            "B": distance_B_min and distance_B_max,
            "C": distance_C_min and distance_C_max
        }

        minDistance = min(handsigns.values())

        print("Distance to minimum A value:", round(distance_A_min, 2),
              "\nDistance to maximum A value:", round(distance_A_max, 2),
              "\nDistance to minimum B value:", round(distance_B_min, 2),
              "\nDistance to maximum B value:", round(distance_B_max, 2),
              "\nDistance to minimum C value:", round(distance_C_min, 2),
              "\nDistance to maximum C value:", round(distance_C_max, 2), "\n")

        for key, value in handsigns.items():
            if minDistance == value:
                print("The gesture is:", key)