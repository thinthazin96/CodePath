# """
# Given an array of integers A sorted in non-decreasing order, return a new array of the squares of each number, also in sorted non-decreasing order.
# """
# def square(arr):
#     result = []
#     for i in arr:
#         result.append(i ** 2)
    
#     return sorted(result)

# print("New square array || Test 1: ", square([-4,-1,0,3,10]) == [0,1,9,16,100])
# print("New square array || Test 2: ", square([-7,-3,2,3,11]) == [4,9,9,49,121])

# """
# Write a function to find if a given integer x appears more than n/2 times in a sorted array of n integers.
# """
# def appear(arr, x):
#     d = {}
#     for i in arr:
#         if i not in d: 
#             d[i] = 1
#         else:
#             d[i] += 1

    
#     if x in d:
#         if len(arr)/2 < d[x]:
#             return True
#         else:
#             return False

# print("Appear more than n/2 times || test 1: ", appear([1, 2, 3, 3, 3, 3, 10], 3) == True)
# print("Appear more than n/2 times || test 2: ", appear([1, 1, 2, 4, 4, 4, 6, 6], 4) == False)
# print("Appear more than n/2 times || test 3: ", appear([1, 1, 1, 2, 2], 1) == True)

