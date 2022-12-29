'''
Given a string s containing characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()"
Output: true

Input: s = "(]"
Output: false
'''
def valid_brackets(tokens):
    mapping = { ')': '(', ']': '[', '}': '{' }

    stack = [] # []

    for token in tokens: # ']' 
        if token not in mapping.keys(): # opening bracket
            stack.append(token)
        else: # closing bracket       #if the stack is not empty, 
            top_element = stack.pop() if stack else None #top_element = '('

            if mapping[token] != top_element: # Not a match  # mapping[']'] != '(' ->  '[' == '('
                return False

    return not stack

def main():
  tests = [
    { 'inputs': ['(',')'],                 'results': True },
    # { 'inputs': ['(',']'],                 'results': False },
    # { 'inputs': ['{','(','[',']',')','}'], 'results': True },
    # { 'inputs': ['(',')','[',']','{','}'], 'results': True },
    # { 'inputs': ['('],                     'results': False },
    # { 'inputs': [')','['],                 'results': False },
  ]

  for i in range(len(tests)):
    print(f'Test {i}:', valid_brackets(tests[i]['inputs']) == tests[i]['results'])

main()