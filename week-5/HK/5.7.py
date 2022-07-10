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