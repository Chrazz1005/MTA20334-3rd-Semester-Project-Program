import numpy as np
import cv2
import math


#######################  Indtil vi får lavet vores egen låner jeg lige Andreas'  ########################
class GaussianBlur:

    def get_gaussian_kernel(kernel_size, std):
        # Gaussian formular:
        # 1/(2*pi*o*o)*e^(-((x*x+y*y)/(2*o*o)))
        # o = std
        kernel = np.zeros(np.asarray([kernel_size, kernel_size]))
        kernel_radius = kernel_size // 2
        for index_x in range(kernel_size):
            x = index_x - kernel_radius
            for index_y in range(kernel_size):
                y = index_y - kernel_radius
                kernel[index_x][index_y] = (
                            1 / (2 * math.pi * std ** 2) * math.exp(-((x ** 2 + y ** 2) / (2 * std ** 2))))
        return np.asarray(kernel)

    def gaussian_blur(img, kernel_size=3):
        assert not kernel_size % 2 == 0, "Kernel size must be odd number"
        kernel = GaussianBlur.get_gaussian_kernel(kernel_size, kernel_size / 6)
        output = cv2.filter2D(img, -1, kernel)
        return np.asarray(output, dtype=np.uint8)





