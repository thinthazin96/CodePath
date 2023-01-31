'''
20. Valid Parentheses || CodePath Week6 Session 1

'''

def isValid(s):
    dic = {'(':')','{':'}','[':']'}
    stack = []
    
    for i in range(len(s)):
        
        for key, value in dic.items(): 
            if s[i] in dict.keys():
                stack.append(s[i])
            else:
                return False
    return True

print(isValid("()"))


