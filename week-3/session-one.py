# # Created a class
# from platform import node
# from this import d


# class CodePath:
#     # init method or constructor
#     def __init__(self,name):
#         self.name = name

#     # created a method that print 
#     def say_hi(self):
#         print("Hello, my name is " , self.name)

# #created an instance or object of that class called 'p'
# p = CodePath('Fleming')
# p.say_hi() #used the method from the class

# #created a class
# class Node:
#     #created a constructor with two parameter and one assign to None value bydefault 
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# first = Node(3)
# print(first.data)

"""
Problem #2: Linked List Cycle
Given a linked list, determine if it has a cycle in it. For simplicity, assume the linked list cannot have more than 1000 nodes in it. 
"""

class LinkedListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head):

    #if there is no two nodes, return False (Note: slow-and-fast-pointer method need two nodes to perform)
    if not head or not head.next :
        return False
    slow = head #slow mover pointer
    fast = head.next # fast mover pointer

    #this ensure that there is two nodes bcz fast node is not null
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        
        else:
            slow = slow.next # slow move by 1 node
            fast = fast.next.next #move by 2 nodes

    return False

#build a linkedlist to test code
node1 = LinkedListNode(1)
node2 = LinkedListNode(2)


#connecting the nodes
node1.next = node2
node2.next = node1 #create a cycle

print(hasCycle(node1)) #should return True bcz it's cycle

node1 = LinkedListNode(1)
print(hasCycle(node1)) #should return False bcz there's one node only

node1 = None
print(hasCycle(node1)) #should return False because there is no node