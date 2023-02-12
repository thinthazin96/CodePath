'''
206. Reverse Linked List

Time Complexity: O(n)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    '''
    2 pointer method:
    1. set prev - > None , current -> head
    2. iterate as long as the head is not null
    3. use temp variable to store the current.next before breaking the link.
    4. break the link by updating current one to previous node.
    5. point current to temp.

    '''
    prev, curr = None, head

    while curr:
        temp = curr.next 
        curr.next = prev
        prev = curr
        curr = temp
    return prev

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
print(reverseList(node1))
