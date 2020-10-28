import numpy as np
import cv2
import math

def meanFilter(img):
    kernelMean = [1 / 3, 1 / 3, 1 / 3]
    kernelSize = len(kernelMean)
    kernelRadius = int(kernelSize / 2)

    inputImg = img
    outputImg = np.zeros_like(inputImg)

    for x in range(len(outputImg) - 2 * kernelRadius):
        total = 0
        for kernel_x, weight in enumerate(kernelMean):
            total += inputImg[x + kernel_x] * weight
        outputImg[x] = total / sum(kernelMean)
    return outputImg

# def get_gaussian_kernel(kernel_size, std):   ### Andreas' kerneludregner
#     # Gaussian formular:
#     # 1/(2*pi*o*o)*e^(-((x*x+y*y)/(2*o*o)))
#     # o = std
#     kernel = np.zeros(np.asarray([kernel_size, kernel_size]))
#     kernel_radius = kernel_size // 2
#     for index_x in range(kernel_size):
#         x = index_x - kernel_radius
#         for index_y in range(kernel_size):
#             y = index_y - kernel_radius
#             kernel[index_x][index_y] = (
#                         1 / (2 * math.pi * std ** 2) * math.exp(-((x ** 2 + y ** 2) / (2 * std ** 2))))
#     return np.asarray(kernel)

def gaussFilter(img):
    kernelGauss = np.asarray([[1, 2, 1],
                             [2, 4, 2],
                             [1, 2, 1]]) * 1/16

    # sigma = (kernelSize - 1) / 6
    #
    # kernelGauss = get_gaussian_kernel(kernelSize, sigma)

    kernelSize = len(kernelGauss)
    kernelRadius = int(kernelSize / 2)

    inputImg = img
    outputImg = np.zeros_like(inputImg )

    for x in range(len(outputImg) - 2 * kernelRadius):
        total = 0
        for kernel_x, weight in enumerate(kernelGauss):
            total += inputImg[x + kernel_x] * weight
        outputImg[x] = total / sum(kernelGauss)
    return outputImg
