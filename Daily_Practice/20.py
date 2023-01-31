'''
20. Valid Parentheses || CodePath Week6 Session 1

Time Complexity: O(1)
'''

def isValid(s):
    mapping = {')':'(','}':'{',']':'['}
    stack = []
    
    for paren in s:
        if paren not in mapping.keys(): #opening bracket
            stack.append(paren)

        else:                           #closing bracket    
            if stack:                   #if the stack is not empty
                top_element = stack.pop()   

                if mapping[paren] != top_element:   #check if the current key's value and stack element is same.
                    return False
            else:                       #if the bracket start with closing bracket and the stack is empty
                return  None            
    return not stack        #if the stack is empty, return False

print('Test 1: ', isValid("]") == None)
print('Test 2: ', isValid("()") == True)
print('Test 3: ', isValid("()[]{}") == True)
print('Test 4: ', isValid("(]") == False)


