import math
from sys import prefix
from unittest import result

def reverse_string(s):
    
    s = s[::-1]
    return s

# print("Problem 1: Reverse string -> ", reverse_string("hello"))

def substring(first_str, sub_str):

    for i in first_str:
        if sub_str in first_str:
            return True
    return False

# print("Problem 2: Substring -> Test 1: ", substring("laboratory", "rat"))
# print("Problem 2: Substring -> Test 2: ", substring("cat", "meow"))

'''
Given a number, return the next smallest prime number.

Planning:
1) If the number is <= 1, return 2 because  2 is the smallest prime number.
2) increment the number by 1 because we are looking for next prime. 
3) run while loop & check if the number is prime.
4) return the number if it is prime, if not increment to next number until we find prime.
'''
def next_prime(num):
    if num <= 1:
        return 2
    
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1): #Must add one to get correct prime
        if num % i == 0:
            return False
    return True

# print("Next Prime | Test 1: ", next_prime(0))
# print("Next Prime | Test 2: ", next_prime(2))
# print("Next Prime | Test 3: ", next_prime(5))
# print("Next Prime | Test 4: ", next_prime(23))

def validPalindrome(s):
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue

            # Found a mismatched pair - try both deletions
            if s[i].lower() != s[j].lower():
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

# print(validPalindrome("A man, a plan, a canal: Panama"))
# print(validPalindrome("race a car"))



def reverse_word(arr):
    arr = "".join(arr)          #Join the array
    arr = arr.split(" ")        #Split it by array to seperate the words
    temp = []                   
    for i in range(len(arr)):   #pop each element 
        temp.append(arr.pop())

    temp = " ".join(temp)

    result = []
    for i in temp:
        result.append(i)
    return result

# print("Reverse Word | Test 1 :", reverse_word(["h","e","l","l","o"," ","w","o","r","l","d"]) == ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'e', 'l', 'l', 'o'])
# print("Reverse Word | Test 2 :", reverse_word(["a"]) == ["a"])
# print("Reverse Word | Test 3 :", reverse_word(["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]) == ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"])

'''
Write a function to evaluate the value of an expression in postfix notation represented by a string with numbers between 0 and 9 and operators separated by whitespace. The expression supports 4 binary operators '+', '*', '-' and '/'.
Input: "5 1 2 + 4 * + 3 -"
Output: 14

Planning:
1) split the string by whitespace & create stack to store numbers only.
2)Loop through the string list and store the number in stack.
3) if we hit operand, pop the last two elements in the stack and do the calculation base on the operand.
4) if len(string) < 2, return the number in stack. [Edge case]
5) store the result of two element back in stack.
6) return the last element left in the stack after the loop.
'''
def post_fix(s):

    s = s.split()
    stack = []

    for i in s:
        if i not in '+-/*':
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return stack.pop()

            firstpop = stack.pop()
            secondpop = stack.pop()
            result = 0

            if i == "+":
                result = secondpop + firstpop
            elif i == "-":
                result = secondpop - firstpop
            elif i == "/":
                result = secondpop / firstpop
            elif i == "*":
                result = secondpop * firstpop

            stack.append(result)

    return stack.pop()

# print("PostFix | Test 1 :", post_fix("5 1 2 + 4 * + 3 -") == 14)
# print("PostFix | Test 2 :", post_fix("5 +") == 5)
# print("PostFix | Test 3 :", post_fix("1") == 1)