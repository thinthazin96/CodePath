'''
Complete the 'condense' function below.
*
* The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
* The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
*/

/*
* For your reference:
*
* SinglyLinkedListNode {
*     int data;
*     SinglyLinkedListNode next;
* }
'''

def condense(head):
    hashSet = set()
    temp = head
    prev = None
    while temp:
        if temp.data not in hashSet:
            hashSet.add(temp.data)
            prev = temp
        else:
            prev.next = temp.next
        temp = temp.next
    return head