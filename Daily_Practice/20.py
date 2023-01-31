'''
20. Valid Parentheses
'''

def isValid(s):
  mapping = {'}': '{', ']': '[', ')' : '('}
  stack = []

  for paren in s:
    if paren not in mapping.keys(): #Add opening in stack
      stack.append(paren)
    else:                          
      if stack:                     #if the stack is not empty
        
        top_elem = stack.pop()
  
        if mapping[paren] != top_elem: #if the closing and opening doesn't match
          return False 

      else:
        return False
  return True

print(isValid("("))

    
    