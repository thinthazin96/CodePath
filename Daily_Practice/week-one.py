import math

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

print("Problem 3: Next Prime -> Test 1: ", next_prime(0))
print("Problem 3: Next Prime -> Test 2: ", next_prime(2))
print("Problem 3: Next Prime -> Test 3: ", next_prime(23))
