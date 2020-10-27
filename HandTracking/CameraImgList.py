
class Node:
    def __init__(self, imagedata):
        self.imagedata = imagedata
        self.nextimg = None


#Frontimg for finding the image in the front.
class CameraQueue:
    def __init__(self):
        self.frontimg = None


    #Throw the shit in the back - method | Queue Data Structure.
    def QueuingNode(self, newpicture):

        NewImage = Node(newpicture)
        if self.frontimg is None:
            self.frontimg = NewImage
            return

        last = self.frontimg
        while (last.nextimg): #Loops through the structure till it's at the last link.
            last = last.nextimg
        last.nextimg = NewImage #adds the image to the chain.


    #Funktion that remove the first element.
    def DeQueingNode(self):
        if self.frontimg is None:
            return None
        else:
            self.frontimg = self.frontimg.nextimg


# SLET RESTEN INDEN AFLEVERING.

#PrintListen Funktion
def listprint(self):
    printval = self.frontimg
    while printval is not None:
        print(printval.imagedata)
        printval = printval.nextimg

list1 = CameraQueue()
list1.frontimg = Node("Test")
e2 = Node("Test2")
e3 = Node("Test3")

#Linking first node to second node.
list1.frontimg.nextimg = e2

#Linking second Node to third node
e2.nextimg = e3


CameraQueue.DeQueingNode(list1)
listprint(list1)


#def RemovingFirstNode(self):

