import math
from wsgiref import validate

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

def next_prime(num):

    if num <= 1:
        return 2 #Becuase Prime number start from 2
    
    num += 1                
    while True:
        if is_prime(num):   
            return num
        num += 1           

#Helper method
def is_prime(num):

    for i in range(2, int(math.sqrt(num)) + 1): #Note: Largest factorial is sqrt(num)
        if num % i == 0:                        #if the num is divisible by i, then it is not prime
            return False
    return True

# print("Problem 3: Next Prime -> Test 1: ", next_prime(0))
# print("Problem 3: Next Prime -> Test 2: ", next_prime(2))
# print("Problem 3: Next Prime -> Test 3: ", next_prime(23))

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

print(validPalindrome("A man, a plan, a canal: Panama"))
print(validPalindrome("race a car"))