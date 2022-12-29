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

# print("Substring | Test 1: ", substring("laboratory", "rat"))
# print("Substring | Test 2: ", substring("cat", "meow"))

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

def appear_once(arr):

    d = {}

    for i in arr:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1

    res = []
    for key, value in d.items():
        if value == 1:
            res.append(key)
            continue
    return res

# print("Appear Once | Test 1 :", appear_once([1,1,2,2,3,4,4]) == [3])
# print("Appear Once | Test 2 :", appear_once([1,2,2,3,4,4]) == [1,3])
# print("Appear Once | Test 3 :", appear_once([1,2,3,4]) == [1,2,3,4])
# print("Appear Once | Test 4 :", appear_once([0]) == [0])
# print("Appear Once | Test 5 :", appear_once([]) == [])
# print("Appear Once | Test 6 :", appear_once([1,1,2,2,3,3,4,4]) == [])

def count_gem(gems, stones):

    if gems == [] or stones == []:              #if one of the list is empty, return None
        return None 
    
    for gem in gems:
        if gem in stones:
    
            gem_count = 0
            d = {}

            for stone in stones:
                if stone in d:
                    d[stone] = d[stone] + 1
                else:
                    d[stone] = 1

            gems = set(gems)

            for stone, n in d.items():
                if stone in gems:
                    gem_count += n
            return gem_count    
        else:
            return None
        
# print("Gem_count in stone | Test 1 :", count_gem(["G", "a"], ["g","g","g","G","A","a","a"]) == 3)
# print("Gem_count in stone | Test 2 :", count_gem([], ["g","g","g","G","A","a","a"]) == None)
# print("Gem_count in stone | Test 3 :", count_gem(["G", "a"], []) == None)
# print("Gem_count in stone | Test 4 :", count_gem(["G", "a"], ["g","g","g","A"]) == None)
# print("Gem_count in stone | Test 5 :", count_gem(["G", "a"], ["G"]) == 1)
# print("Gem_count in stone | Test 6 :", count_gem(["G"], ["G"]) == 1)


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

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

Planning:
1) loop through the list and find the compliment.
2) create a dictionary and store the current value and its index if the compliment does not exist.
3) if yes, return the current index and the value of the compliment from the dictionary.
'''
def twoSum(arr, target):

    d = {}
    for i in range(len(arr)):
        compliment = target - arr[i]
        if compliment not in d:
            d[arr[i]] = i
        else:
            return [d[compliment],i]

print("Two Sum | Test 1: ", twoSum([1,2,5,7],9) == (1,3))
print("Two Sum | Test 2: ", twoSum([3,3],6) == (0,1))
