import numpy as np
import cv2
import math


def meanFilter(img):  ##primitive 1D averaging filter
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


def primitiveGauss(img):  # very primitive weighted averaging 1D
    kernelG = [1 / 3, 2 / 3, 1 / 3]
    kernelSize = len(kernelG)
    kernelRadius = int(kernelSize / 2)

    inputImg = img
    outputImg = np.zeros_like(inputImg)

    for x in range(len(outputImg) - 2 * kernelRadius):
        total = 0
        for kernel_x, weight in enumerate(kernelG):
            total += inputImg[x + kernel_x] * weight
        outputImg[x] = total / sum(kernelG)
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

# def matrixGauss(img):
#     kernelGaussx3 = np.asarray([[1, 2, 1],
#                                 [2, 4, 2],
#                                 [1, 2, 1]])
#
#     kernelGaussx5 = np.array([[1, 4, 7, 4, 1],
#                               [4, 16, 26, 16, 4],
#                               [7, 26, 41, 26, 7],
#                               [4, 16, 26, 16, 4],
#                               [1, 4, 7, 4, 1]])
#
#     kernelSize = len(kernelGaussx5)
#
#     kernelRadius = math.floor(kernelSize / 2)
#
#     inputImg = img
#     outputImg = np.zeros_like(inputImg)
#     # outputImg = np.array([[np.zeros(inputImg.shape[0] - 2 * kernelRadius)], [np.zeros(inputImg.shape[1] - 2 * kernelRadius)]])
#     print(kernelGaussx5)
#     print(outputImg.shape)
#     print(outputImg.size)
#
#     for x in range(outputImg.shape[0]):
#         for y in range(outputImg.shape[1]):
#
#             inputSlice = inputImg[y:y + kernelSize][x:x + kernelSize]
#             outputImg[y][x] = sum(inputSlice * kernelGaussx5) / sum(kernelGaussx5)
#
#     return outputImg


if __name__ == '__main__':
    img = cv2.imread('fstretch.jpg', 0)
    img2 = cv2.imread('handTest.png', 0)

    # gaussImg = gaussFilter(img)
    # meanImg2 = meanFilter(img2)

    # matrixG = matrixGauss(img2)
    mean = meanFilter(img2)
    gauss = primitiveGauss(img2)
    # cv2.imshow('Gauss?', gaussImg)
    # cv2.imshow('mean', meanImg2)
    cv2.imshow('mean', mean)
    cv2.imshow('gauss', gauss)
    cv2.imshow('Normal', img2)
    cv2.imshow('matrix', img2)
    # cv2.imshow('Gauss', gaussImg)
    cv2.waitKey()
    cv2.destroyAllWindows()
