Import Node

class CameraImgList:
    def __init__(self):
        self.headval = None

list1 = CameraImgList()
list1.headval = Node("Test")
e2 = Node("Test2")
e3 = Node("Test3")

#Linking first node to second node.
list1.headval.nextval = e2

#Linking second Node to third node
e2.nextval = e3

def listprint(self):
    printval = self.headval
    while printval is not None:
        print(printval.dataval)
        printval = printval.nextval

def QueuingNode(self, newpicture):
    NewNode = Node(newpicture)
    if self.headval is None:
        self.headval = NewNode
        return
    laste = self.headval
    while(laste.nextval):
        laste = laste.nextval
    laste.nextval=NewNode


