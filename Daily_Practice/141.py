'''
141. Linked List Cycle

Time Complexity: O(n)
'''
class ListNode:
    def __init__(self,val, next):
        self.val = val
        self.next = None
        
def hasCycle(head):
    '''
    1. create fast and slow pointer both starting at the head.
    2. iterate as long as fast pointer and fast.next pointer is not null to cover the single node Edge case.
    3. slow pointer move by one and fast pointer move by two.
    4. if slow and fast pointer meet at some point, return True.
    5. if slow and fast pointer don't meet at some point, return False.
    '''

    slow , fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False