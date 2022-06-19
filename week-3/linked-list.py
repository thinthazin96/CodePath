# Crated a Node for singly linked list
class Node:
    #Constructor with data and None by default.
    def __init__(self, data = None, next = None):
        self.data=data
        self.next=next

# a linked list class with a single head node
class LinkedList:
    def __init__(self):
        #head is None by default
        self.head = None

    #insertion method for the linked list
    def insert(self, data):
        #create an obj using Node class
        newNode = Node(data)
        #Check if the head is None or not, if it is True that head is None.
        if(self.head):
            #assing that head as current node
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()

