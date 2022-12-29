'''
Given a list of integers, remove any nodes that have values that have previously occurred in the list and retrun a reference to the head of the list.

Eg: 
Input: 3 -> 4 -> 3 -> 6
Output: After removing redundant nodes: 3 -> 4 -> 6
* For your reference:
*
* SinglyLinkedListNode {
*     int data;
*     SinglyLinkedListNode next;
* }
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def condense(head):
    hashSet = set()
    temp = head
    prev = None
    while temp:                         #loop if temp is not None
        if temp.data not in hashSet:    
            hashSet.add(temp.data)      #add the data in headSet if it doesn't already exist.
            prev = temp                 #store current temp in prev
        else:
            prev.next = temp.next       #store temp.next in prev.next if it already exist
        temp = temp.next                #go to next node
    return head                         #return head

#Create Nodes
Node1 = Node(3)
Node2 = Node(4)
Node3 = Node(3)
Node4 = Node(6)

#Connect Nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4


print(condense(Node1))