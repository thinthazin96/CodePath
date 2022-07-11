'''
Seperate the odd and even base on the node not on the value.

Input:  1->2->3->4->5
Output: 1->3->5->2->4

Input:  2->1->3->5->6->4->7
Output: 2->3->6->7->1->5->4

Planning:

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next

def oddEvenList(head):
    if (head != None):
        odd = head
        even = head.next
        evenHead = even

        while (even != None and even.next != None):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = evenHead    # BUG ON THIS LINE
    return head

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

printList(oddEvenList(Node1))