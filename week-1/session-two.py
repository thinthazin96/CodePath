"""
Given an integer n, print the nth terms in the Fibonacci sequence.

Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...

***Question to ask:***

1. Can the input be less than 1?
2. Is there a max integer?
3. Do we need to return anything? Or only print?
4. 0th and 1st terms are 0 and 1 respectively?

***Plan/ Pseudocode***

5th = 4th + 3rd
4th = 3rd + 2nd
3rd = 2nd + 1st

fib(5) = fib(4) + fib(3)
fib(4) = fib(3) + fib(2)
fib(3) = fib(2) + fib(1)
fib(n) = fib(n-1) + fib(n-2)

**Base case: **

if n = 1 -> 0
if n = 2 -> 1
"""


def fibonacci(n):
    assert n > 0

    #base case
    if n == 1:
        return 0
    
    if n == 2:
        return 1

    #recursive call
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iteration(n):
    first_element = 0
    second_element = 1

    if n > 0:
        #Check if the input is one number.
        if n == 1:
            #if yes, return 0
            return first_element
        
        #Check if the input is two number.
        if n == 2:
            #if yes, return 1
            return second_element

        #if the input is more than two number,
        else:
            #loop from 3rd index through the input number + 1
            for i in range(3, n+1):
                #Store the additon of first_element and second_element in a result variable.
                result = first_element + second_element
                #Swap the second_element value to first_element
                first_element = second_element
                #Swap the result to the second_element
                second_element = result

            print(result)



fibonacci_iteration(6)
# print(fibonacci_iteration(6))