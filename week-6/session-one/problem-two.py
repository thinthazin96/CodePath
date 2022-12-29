'''
Design a stack class that allows you to push in values, pop out values, 
and retrieve the smallest value inside the stack.
'''

class MinStack:

  def __init__(self, l):                #stack structure
    self.min_stack = []                 #to store minimum value
    self.stack = []                     #to element in the list
    for i in l: self.push(i)            #calling push each element from the list into the stack
  
  def push(self, i):                    #push function
    self.stack.append(i)                #append each element into stack list
    if not(self.min_stack) or i <= self.min_stack[-1]:  #Check if min_stack is empty or 'i' is less than or equal to the 'last element' in min_stack
      self.min_stack.append(i)          #if yes, append that element to stack
  
  def pop(self):                        #pop function
    removed = self.stack.pop()          #store removed element in a variable
    if removed == self.min_stack[-1]:   #Check if the removed element value is equal to the last element in min_stack
      return self.min_stack.pop()       #if yes, return removed element value of min_stack

  def get_min(self):                    #this function returns the minimum value of the list
    return self.min_stack[-1] if self.min_stack else None #if min_stack is not empty return the last element of the min_stack, else return None
    
def main():
#   s = MinStack([])
#   print('Test 0:', s.get_min() == None)

#   s = MinStack([1])
#   print('Test 1:', s.get_min() == 1)

  s = MinStack([2,1])
  print('Test 2:', s.get_min() == 1)
  
#   s = MinStack([1,2])
#   print('Test 3:', s.get_min() == 1)
  
#   s = MinStack([2,3])
#   print('Test 4:', s.get_min() == 2)
  
#   s = MinStack([3,2,1])
#   print('Test 5:', s.get_min() == 1)
  
#   s = MinStack([1,2,3])
#   print('Test 6:', s.get_min() == 1)  

#   s = MinStack([2,1,1])
#   print('Test 7:', s.get_min() == 1)
  
  s = MinStack([2,1,1])
  s.pop()
  print('Test 8:', s.get_min() == 1)

#   s = MinStack([2,3,1])
#   s.pop()
#   print('Test 9:', s.get_min() == 2)

#   s = MinStack([2,3,1,4])
#   s.pop()
#   print('Test 10:', s.get_min() == 1)
  
main()