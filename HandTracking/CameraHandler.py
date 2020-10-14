import time

import cv2
import numpy as np


class CameraHandler:
    __cap = 0

    def __init__(self, capture):
        self.__cap = capture

    def grabFrame(self):
        fps = self.__cap.get(cv2.CAP_PROP_FPS)  # Gets the frames per second
        frames = []

        success, image = self.__cap.read()
        count = 0
        cv2.imshow('video', image)

        while success:
            success, image = self.__cap.read()

            frames.append(cv2.imwrite("frame%d.jpg" % count, image))  # save frame as JPEG file

            print('Read a new frame: ', success)
            count += 1
            print('fps', fps)
            time.sleep(5)
            print('length of frames array', len(frames))

        return frames
