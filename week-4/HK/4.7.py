'''
Given a linked list, swap every two adjacent nodes and return its head.

Given: 1->2->3->4
Output: 2->1->4->3

Match: 
Dummy head 



'''
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next

def swapNodesInPairs(head: ListNode):
    dummyHead = ListNode(0)
    dummyHead.next = head
    p = dummyHead
    while(p.next != None and p.next.next != None):
        # use first to track first node
        first = p
        p = p.next
        first.next = p.next
        
        # use second to track next node of the pair
        second = p.next.next
        p.next.next = p
        p.next = second
    return dummyHead.next

Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)
Node6 = ListNode(6)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6

printList(swapNodesInPairs(Node1))