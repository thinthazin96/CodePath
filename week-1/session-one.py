"""
Problem 1 Reverse a String

Input: "hello"
Output: "olleh"
"""
#using string method
input_str = input("Enter here: ")
# print(input_str[::-1])

#Using isnumeric() method
def reverse_string(string):
  #empty string to store the reverse string
  result = ""

  #Return the input string back if the input is empty
  if string == "":
    return string

  #Return the msg if the input is integer. isnumeric() check for integer and doesn't take parameter.
  elif string.isnumeric():
    return "Please enter letter only."

  #if the input is a string
  else:
    #create a list to store each letter of a input word.
    str_lst = []
    #loop through the input string
    for i in string:
      #Add each of the letter into a new list
      str_lst.append(i)

    #start the loop from len(str_lst)-1 to -1 and decrement by -1
    for i in range(len(str_lst)-1, -1, -1):
      #Add each letter into an empty string to create a reverse string
      result = result + str_lst[i]

    #Return the reverse string
    return result

#calling reverse_string function
print(reverse_string(input_str))

#using try & execpt method 
def reverse_string_try(string):
  #empty string to store the reverse string
  result = ""
  #set isInt to False 
  isInt = False
  
  try:
    #convert the input string to integer
    int(string)
  #Raise error only if isInt is True
  except ValueError:
    isInt = True
  #if it is true that the input string is not an integer
  if isInt:
    #create a list to store each letter of a input word.
    str_lst = []
    #loop through the input string
    for i in string:
      #Add each of the letter into a new list
      str_lst.append(i)

    #start the loop from len(str_lst)-1 to -1 and decrement by -1
    for i in range(len(str_lst)-1, -1, -1):
      #Add each letter into an empty string to create a reverse string
      result = result + str_lst[i]

    #Return the reverse string
    return result

  #if it is true that input string is an integer
  else:
    #Return error message
    return "Please enter letter only."

print(reverse_string_try(input_str))
    
  
"""
Bonus Problem: Substring

Input: laboratory, rat
Output: true

Input: cat, meow
Output: false
"""

substr = input("Enter a string: ")

def substring(string):
  #Split the string from ", " and store in a variable.
  split_str = string.split(", ")
  #Store the 1st element of split_str list in a variable.
  first_str = split_str[0]
  #Store the 2nd element of second_str list in a variable.
  second_str = split_str[1]
  #If the substring exit in string.
  if second_str in first_str:
    return True
  #if the substring doesn't exit in the string,
  else:
    return False

print(substring(substr))

"""
Given a number, return the next smallest prime number

Note: A prime number is greater than one and has no other factors other than 1 and itself. 

"""
# def next_prime(n):
#   if n > 1:
#     if n / n == 1 and n % n == 0:
    
  