class LinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def partition(head, x):
    beforeHead = before = LinkedListNode(0)
    afterHead = after = LinkedListNode(0)
    while head != None:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    before.next = afterHead.next
    after.next = None
    return beforeHead.next

node1 = LinkedListNode(1)
node2 = LinkedListNode(4)
node3 = LinkedListNode(3)
node4 = LinkedListNode(2)
node5 = LinkedListNode(5)
node6 = LinkedListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(partition(node1,3))