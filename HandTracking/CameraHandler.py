import time

import cv2
import numpy as np

#two __ = privat instead of public.

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

            #Making a "Queue List" aka. insertion at back, deletion in front.
            if frames >= [5]:
                frames.pop(0)


            print('Read a new frame: ', success)
            count += 1
            print('fps', fps)
            time.sleep(5)
            print('length of frames array', len(frames))

        return frames
