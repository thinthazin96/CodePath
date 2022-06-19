# Created a class
class CodePath:
    # init method or constructor
    def __init__(self,name):
        self.name = name

    # created a method that print 
    def say_hi(self):
        print("Hello, my name is " , self.name)

#created an instance or object of that class called 'p'
p = CodePath('Fleming')
p.say_hi() #used the method from the class

#created a class
class Node:
    #created a constructor with two parameter and one assign to None value bydefault 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

first = Node(3)
print(first.data)

"""
Problem 1: Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.
Input: 1->1->2  
Output: 1->2  

Input: 1->1->2->3->3  
Output: 1->2->3 

Understand:

"""