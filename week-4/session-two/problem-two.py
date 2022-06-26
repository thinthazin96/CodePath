#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
# Input: 1->2
# Output: false
#
# Example 2:
# Input: 1->2->2->1
# Output: true


import re


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(node):
    fullLength = getLength(node) # fullLength = 3
    
    if fullLength == 0:
        return True

    firstHalf = []
    currentNode = 0
    while currentNode < (fullLength // 2): # 0 < 1
        firstHalf.append(node.val) # firstHalf = [1]
        node = node.next    # node at 1 -> 2
        currentNode += 1    # currentNode = 1

    # To skip the middle node 2
    if fullLength % 2 == 1: # 3 % 2 == 1
        node = node.next    # node at 1 -> 2 -> 3


    while node: # if the node is not None
        currentNode -= 1 # currentNode = 0th
        if node.val != firstHalf[currentNode]: # 3 != 1
            return False
        node = node.next

    return True


def getLength(node):
    length = 0
    while node != None:
        length += 1

        if node.next == None:
            return length
        node = node.next
    return length


class Tests:
    if __name__ == "__main__":
        #0
        n0_1 = None
        print(f"Test 0 - isPalindrome returned: {isPalindrome(n0_1)}, expected: True")

        # 1
        n1_1 = ListNode(val=1)
        print(f"Test 1 - isPalindrome returned: {isPalindrome(n1_1)}, expected: True")

        # 1 -> 2
        n2_1 = ListNode(val=1)
        n2_2 = ListNode(val=2)
        n2_1.next = n2_2
        print(f"Test 2 - isPalindrome returned: {isPalindrome(n2_1)}, expected: False")

        # 1 -> 2 -> 3
        n3_1 = ListNode(1)
        n3_2 = ListNode(2)
        n3_3 = ListNode(3)
        n3_1.next = n3_2
        n3_2.next = n3_3
        print(f"Test 3 - isPalindrome returned: {isPalindrome(n3_1)}, expected: False")

        # 1 -> 2 -> 1
        n4_1 = ListNode(1)
        n4_2 = ListNode(2)
        n4_3 = ListNode(1)
        n4_1.next = n4_2
        n4_2.next = n4_3
        print(f"Test 4 - isPalindrome returned: {isPalindrome(n4_1)}, expected: True")
