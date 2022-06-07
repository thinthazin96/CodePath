"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Note: Natural numbers doesn't include 0.
Find the sum of all the multiples of 3 or 5 below 1000.

***Plan***
1. create an empty list to store the multiples of 3 or 5.
2. loop from 0 to 1000.
3. if the number is multiples of 3 or 5, store it in the list.
4. Add the numbers in the list and return sum.
"""

def multiples():
    result = []
    for i in range(1, 1000):
        if 3 * i == i:
            result.append(i)
    
    sum = 0
    for i in result:
        sum = sum + i 
    
    return sum

print(multiples())