from platform import node


class Node(object):
    def __init__(self, v):
        self.val = v
        self.next = None

def delete_node(head, val):
    d = Node("dummy") #created dummy head
    d.next = head #assign head as next node of dummy which made dummy head node
    p = d   #assign dummy in a variable
    c = head 
    while c:
        if c.val == val: # if head.val is equal to the value
            p.next = c.next #head.next is dummy node next
            return d.next
        p = c
        c = c.next
    return d.next
