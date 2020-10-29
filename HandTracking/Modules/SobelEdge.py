
import cv2
import numpy as np
from HandTracking.Modules.GaussianBlur import *

class SobelEdge:
    __img = 0
    gxKernelArray = np.array(([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]), np.float32)
    gyKernelArray = np.array(([1, 2, 1], [0, 0, 0], [-1, -2, -1]), np.float32)


    def __init__(self, img):
        self.__img = gaussFilter(img)


    def detectionLoop(self):
        n, m, d = self.__img.shape


        edge_img = np.zeros_like(self.__img)

        for row in range(3,
                         n - 2):  # It is  above the range 0 to end, because we ignore the edges of the image since the kernel might not fit
            for col in range(3, m - 2):
                local_pixels = self.__img[row - 1:row + 2, col - 1:col + 2, 0]  # defining 3x3 box for checking the img

                trans_pixels = self.gyKernelArray * local_pixels  # multiply box with vertical kernel array
                vert_score = trans_pixels.sum() / 4  ##ift. +4 og /8 - Our kernel returns a value between -4 and 4, we want to map the from 0-1.

                hori_pixels = self.gxKernelArray * local_pixels
                hori_score = hori_pixels.sum() / 4

                edge_score = (vert_score ** 2 + hori_score ** 2) ** 0.5
                edge_img[row, col] = [edge_score] * 3

        edge_img = edge_img / edge_img.max()



        return edge_img

