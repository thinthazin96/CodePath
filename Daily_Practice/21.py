'''
21. Merge Two Sorted Lists

Time Complexity: O(n)
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(list1, list2):
        '''
        1. create Dummy node
        2. iterate as long as both list1 and list2 are not empty.
        3. if list1.val < list2.val: add the list1.val to the tail of dummy node.
        4. else list1.val > list2.val: add the list2.val to the tail of dummy node.
        5. update the tail pointer evertime a node is added.
        6. if list1 is not empty, add whatever left in list1 to the tail.
        7. else list2 is not empty, add whatever left in list2 to the tail.
        8. return the next elements of dummy node.
        '''
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next

            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next