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


print(fibonacci(6))