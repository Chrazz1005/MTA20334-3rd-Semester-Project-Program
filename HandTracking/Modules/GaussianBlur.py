import numpy as np
import cv2
import math


def meanFilter(img):
    kernelMean = [1 / 3, 1 / 3, 1 / 3]
    kernelSize = len(kernelMean)
    kernelRadius = int(kernelSize/2)

    inputImg = img
    outputImg = np.zeros_like(inputImg)

    for x in range(len(outputImg) - 2 * kernelRadius):
        total = 0
        for kernel_x, weight in enumerate(kernelMean):
            total += inputImg[x + kernel_x] * weight
        outputImg[x] = total/sum(kernelMean)
    return outputImg

def gaussFilter(img):
    kernelGauss = [1 / 4, 1 / 2, 1 / 4]
    kernelSize = len(kernelGauss)
    kernelRadius = int(kernelSize / 2)

    inputImg = img
    outputImg = np.zeros_like(inputImg)

    for x in range(len(outputImg) - 2 * kernelRadius):
        total = 0
        for kernel_x, weight in enumerate(kernelGauss):
            total += inputImg[x + kernel_x] * weight
        outputImg[x] = total / sum(kernelGauss)
    return outputImg
