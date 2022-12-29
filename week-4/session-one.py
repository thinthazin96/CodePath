'''
Problem 1: Remove Nth Node from End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Input: 1->2->3->4->5, n = 2
Output: 1->2->3->5

Explanation: We remove the second node from the end, the node with value 4

Understand:
Edge Cases:
if n > len of nodes, return None
if n <= 0, return None
if the list of nodes is empty, return None
if len of nodes is 1, return None

Match:
two-pointers
multiple passes: 
1) get the length of the nodes
2) substract n-th node from the length of the nodes -> len(nodes) - n

Plan:
create a function that returns the length of the nodes

'''
#create a class Node
class Node:
    #create constructor
    def __init__(self, val):
        self.val = val
        self.next = None

#this function return the length of the nodes
def getLength(node):
    #initialize the count
    count = 0
    while(node):    # this is same as while(node != None):
        count += 1
        node = node.next    #next node become current node
    return count

def remove_nth_node(head, n):


    if head.next == None:
        return None
    elif n <= 0:
        return None

    len_nodes = getLength(head)
    
    if n > len_nodes:
        return None

    deleteIndex = len_nodes - n
    temp = head

    if deleteIndex == 0:
        return temp.next

    for i in range(deleteIndex-1):
        temp = temp.next
    temp.next = temp.next.next

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

ll = remove_nth_node(head, 7)

while head:
    print(head.val)
    head = head.next





