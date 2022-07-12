'''
Problem 3 - Sort a stack using a temporary stack (bonus)
Write a program to sort a stack such that the smallest items are on top. You can use an additional temporary stack, but you may not copy elements into any other data structure (such as an array).

The stack supports the following operations : push, pop, peek, isEmpty.

Input and output are both stacks

Input : [34, 3, 31, 98, 92, 23]
Output : [3, 23, 31, 34, 92, 98]

Input : [3, 5, 1, 4, 2, 8]
Output : [1, 2, 3, 4, 5, 8]

Understand: 
input -> list, output -> list in ascending order
Edge case:
What if the all the numbers are same?
What if the list is empty?
What if the input is string? [Optional]

Match: Stack

Planning:
1. Create an additional temporary Stack.
2. While input stack is NOT empty do:
3. Pop an element from input stack called temp.
4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
5. Pop from temporary stack and push it to the input stack.
6. Push temp in temporary stack.
7. In the end, the sorted numbers are in the temporary Stack.

Time Complexity: O(N^2)
Space Complexity: O(N)

Not optimal solution

'''
def sortStack(input):
    print("Given:", input)
    # 1. Create an additional temporary Stack.
    tempStack = []

    # 2. While input stack is NOT empty do:
    while len(input) != 0:
        # 3. Pop an element from input stack called temp.
        temp = input.pop()

        # 4. While temporary stack is NOT empty and top of temporary stack is greater than temp:
        while len(tempStack) != 0 and tempStack[len(tempStack)-1] > temp:
            # 5. Pop from temporary stack and push it to the input stack.
            input.append(tempStack[len(tempStack)-1])
            tempStack.pop()

        # 6. Push temp in temporary stack.
        tempStack.append(temp)

    print("Sorted: ", tempStack)
    # 7. In the end, the sorted numbers are in the temporary Stack.
    return tempStack

print(f'Test 1:', sortStack([3, 5, 1, 4, 2, 8]) == [1, 2, 3, 4, 5, 8])