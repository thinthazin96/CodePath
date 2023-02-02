'''
22. Generate Parentheses

Add open bracket if open < n
Add closing bracket if close < n
Done if openN == closeN == n
'''
def generateParenthesis(n):
  stack = []
  res = []

  def backtrack(openN, closedN):
    if openN == closedN == n:
      res.append("".join(stack))
      return

    if openN < n:                   #openN start from 0 
      stack.append("(")
      backtrack(openN + 1, closedN) #One open bracket already exit in stack, therefore openN + 1
      stack.pop()                   #old generated pair must be pop to put the new one in

    if closedN < openN: 
      stack.append(")")
      backtrack(openN, closedN + 1)
      stack.pop()                  #old generated pair must be pop to put the new one in

  backtrack(0,0)
  return res      #Return the res, if nth in stack to pop & both open and close is 0.

print(generateParenthesis(2))
  