'''
155. Min Stack

Time Complexity: O(1)

'''

class MinStack:

    def __init__(self):
      self.stack = []
      self.minStack = []
        
    def push(self, val) -> None:
      self.stack.append(val)
      val = min(val, self.minStack[-1] if self.minStack else val) #if minStack is not empty, take its top value, else take current element to find minimum value
      self.minStack.append(val)

    def pop(self) -> None:
      self.stack.pop()
        
    def top(self) -> int:
      return self.stack[-1]
        
    def getMin(self) -> int:
      return self.minStack[-1]
        