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
        result.append(3 * i)
        result.append(5 * i)

    result = set(result)
    sum = 0
    for i in result:
        if i < 1000:
            sum = sum + i 
            print(i)
    return sum

# print(multiples())

#---------Hacker Rank Assignments--------------------------------
def fizzbuzz(nums):
    for i in nums:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# print(fizzbuzz([3,5,15,2,10]))

def fibonacci(n):
    
    #create a list with 0 and 1    
    seq=[0,1]
    #loop from 2 through n+1
    for i in range(2,n+1):
        #Append the sum of i-1 and i-2 to the list
        seq.append(seq[i-1]+seq[i-2])
    #return the elemnt of nth index from the list
    return seq[n]

print(fibonacci(7))
