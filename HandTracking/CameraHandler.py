import time
import cv2
import numpy as np

# # #two __ = privat instead of public.
class CameraHandler:
    __cap = 0

    def __init__(self, capture):
        self.__cap = capture

    def grabFrame(self):

        success, image = self.__cap.read()
        cv2.imshow('video', image)
        cv2.imwrite("frame.jpg", image)  # save frame as JPEG file
#
# class CameraHandler:
#     __cap = 0
#
#
#     def __init__(self, capture): #Ændre kamera
#         self.__cap = capture
#
#     # def grabFrame(self,list):
#     #     #fps = self.__cap.get(cv2.CAP_PROP_FPS)  # Gets the frames per second
#     #     #frames = []
#     #     self.__cap = cv2.VideoCapture(0)
#     #     CameraQueue = clist.CameraQueue()
#     #     Node = clist.Node()
#     #
#     #     success, image = self.__cap.read()
#     #     count = 0
#     #     cv2.imshow('video', image)
#     #
#     #     while success:
#     #         success, image = self.__cap.read()
#     #
#     #         i = Node(cv2.imwrite("frame%d.jpg" % count, image))
#     #
#     #         CameraQueue.QueuingNode(list, i) # save frame as JPEG file
#     #
#     #         count += 1 #Lav som et loop bare sørg for at billederne før det er slettet.
#     #         time.sleep(5)
#     #
#     #         print('Read a new frame: ', success)
#     #         print('length of frames array', len(list)) #Len returns number of items in an object
#     #
#     #     return
#
#         def grabFrame(self):
#             #fps = self.__cap.get(cv2.CAP_PROP_FPS)  # Gets the frames per second
#             #frames = []
#             __cap = cv2.VideoCapture(0)
#             CameraQueue = clist.CameraQueue()
#             Node = clist.Node()
#
#             success, image = __cap.read()
#             count = 0
#             cv2.imshow('video', image)
#
#             while success:
#                 success, image = __cap.read()
#
#                 i = Node(cv2.imwrite("frame%d.jpg" % count, image))
#
#                 CameraQueue.QueuingNode(self, i) # save frame as JPEG file
#
#                 count += 1 #Lav som et loop bare sørg for at billederne før det er slettet.
#                 time.sleep(5)
#
#                 print('Read a new frame: ', success)
#                 print('length of frames array', len(list)) #Len returns number of items in an object
#
#             return
#
# cap = cv2.VideoCapture(0)
# c = CameraHandler(cap)
# c.grabFrame(list)

# class CameraHandler():


    # def __init__(self,):

    #  QueuingNode(list, image)
    # def grabFrame(self, list):
    #     self.list = list
    #     cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #
    #     success, image = cap.read()
    #
    #     np_image = np.array(image)
    #     #np_image = cv2.imread('video', image)
    #     clist.QueuingNode(list,np_image)
    #     #np_image = np.array(image)
    #     #print(len(image))
    #     #cv2.imshow('video', image)
    #     cap.release()
    #
    #     return image

# list = CameraHandler()
# list.grabFrame()
# print(CameraHandler.grabFrame())

#             print('Read a new frame: ', success)
#             count += 1
#
#             time.sleep(5)
#             print('length of frames array', len(frames))


#Virker, men ikke med data strukture:

#two __ = privat instead of public.


