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
        newNode = Node(data) #create an obj using Node class
        if(self.head): #if it is True that self.head is not None, then
            #assing that head as current node
            current = self.head
            while(current.next): #if current.next is not None, then
                current = current.next
            current.next = newNode #set the newNode to the current.next node
        else:#if self.head is None, then
            self.head = newNode #newnode become self.head

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

