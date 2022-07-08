'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Understand:
what if the linked list is empty?
what if k == 0?

 
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
    
def get_len(node):
    len_node = 0  
    while node:
        len_node += 1
        node = node.next

    return len_node

def printList(node):
    while node is not None:
        print(node.val, end=" ")
        node = node.next

def roateList(head, k):

    len_node = get_len(head)

    curNode = head
    

    for i in range(k):
        
        while curNode and curNode.next:
            temp = curNode.next.val
            curNode.next.val = curNode.val
            curNode = curNode.next

    return head

list1 = Node(1)
list2 = Node(2)
list3 = Node(3)
list4 = Node(4)
list5 = Node(5)

list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list1 #create a cycle

# printList(list1)
printList(roateList(list1,2))
