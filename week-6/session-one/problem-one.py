'''
Problem #1: Evaluate Postfix expression
Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators '+', '*', '-' and '/'.

Note: Arithmetic Expressions can be written in Infix, Prefix or Postfix notations.

Postfix notations keep operators after operands. A postfix expression for the examples above would be “3 4 +”.

Input: "5 1 2 + 4 * + 3 -"
Output: 14

The expression is evaluated as follows:
5 3 4 * + 3 -
5 12 + 3 -
17 3 -
14

Understand:
1. input: string type with whitespace inbetween
2. Inside stirng: 0-9, four operands '+-*/'
Edge case: 1 +, 1 , " " : len(arry) < 2: return stack. pop()

Match:
Stack

Planning:
1. split the input string and store it in a variable
2. create a stack [empty list]
3. loop through the list until we hit the operands
4. convert the each elements

'''

def eval_rpn(s):
  tokens = s.split() #take off whitespace and store each element in list.

  stack = [] #To store numbers only
  
  for token in tokens:          #loop through the list
    if token not in '+-/*':     #Check if the element is operands
      stack.append(int(token))  #if not, parse the element from string to integer and add into stack. [1]
      continue  

    if len(stack) < 2: return stack.pop() 

    r_op = stack.pop()
    l_op = stack.pop()
    result = None

    if   token == '+': result = l_op + r_op
    elif token == '-': result = l_op - r_op
    elif token == '*': result = l_op * r_op
    elif token == '/': result = int(l_op / r_op)
      
    stack.append(result)

  return stack.pop()
    
def main():
  tests = [
    { 'inputs': '3 2 +',      'results': 5 },
    { 'inputs': '2 1 + 3 *',  'results': 9 },
    { 'inputs': '4 13 5 / +', 'results': 6 },
    { 'inputs': '2',          'results': 2 },
    { 'inputs': '5 +',        'results': 5 },
    { 'inputs': '5 1 2 + 4 * + 3 -', 'results': 14 },
  ]

  for i in range(len(tests)):
    print(f'Test {i}:', eval_rpn(tests[i]['inputs']) == tests[i]['results'])

main()