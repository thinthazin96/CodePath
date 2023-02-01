'''
150. Evaluate Reverse Polish Notation

Time Complexity: O(1)
'''
def evalRPN(tokens):
    stack = []
    operands = '+-*/'

    for token in tokens:
        if token not in operands:
            stack.append(int(token))
        else:
            first_element = stack.pop()
            second_element = stack.pop()

            if token == "+":
                answer = second_element + first_element
            elif token == "-":
                answer = second_element - first_element
            elif token == "*":
                answer = second_element * first_element
            elif token == "/":
                answer = int(second_element / first_element)

            stack.append(answer)
    
    return stack.pop()


# print("Test 1: ", evalRPN(["2","1","+","3","*"]) == 9)
# print("Test 2: ", evalRPN(["2"]) == 2)
print("Test 3: ", evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)