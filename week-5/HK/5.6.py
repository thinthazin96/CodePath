'''
Write a method that finds the node at which the intersection of two singly linked lists begins. 
If the two linked lists don't intersect, return null. Your algorithm should have linear time complexity and constant space complexity.

Input: listA = 0->9->1->2->4, listB = 3->2->4
Output: Reference of the node with value = 2

Planning:
1. create a function that return the length of the list
2. get length of each list
3. assign to small and large base on thier length
4. find the difference between the two lists 
5. Move the pointer for larger up to the differenc
6. move both pointer until they match
'''

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def findlength(head):
  count = 0
  while head:
    count += 1
    head = head.next
  return count
  
def findIntersection(listA, listB):
  lengthA = findlength(listA)
  lengthB = findlength(listB)

  difference = abs(lengthA - lengthB)
  
  if lengthA > lengthB:
    tempLonger = listA
    tempShorter = listB
  else:
    tempLonger = listB
    tempShorter = listA

  count = 0
  while count < difference:
    tempLonger = tempLonger.next
    count += 1

  while tempLonger:
    if tempLonger.val == tempShorter.val:
      return tempLonger.val
    tempLonger = tempLonger.next
    tempShorter = tempShorter.next
    
  return None

# listA = 0->9->1->2->4
# listB = 3->2->4
  
listA = Node(0)
listA.next = Node(9)
listA.next.next = Node(1)
listA.next.next.next = Node(2)
listA.next.next.next.next = Node(4)

listB = Node(3)
listB.next = Node(2)
listB.next.next = Node(4)

print(findIntersection(listA, listB))