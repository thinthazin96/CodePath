"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
"""
"""
Ask Interviewer = Are the number going to be adjacent?

U - input is a list and return a list of indices that add up to target.

M - Dictionary / Hash Map

Planning:
create a dictionary to track of the complimentary
1) loop throught the list
2) find the complimentary by target - arr[i]
3) store the arr[i] as key and its index as value
4) if the complimentary exists in the list return the current index and the value of the complimentary.
5) else add that into the dictionary.
"""
def two_sum(arr, target):
    d = {}            
    for i in range(len(arr)): 
        compliment = target - arr[i]
        if compliment in d:
            return [d[compliment], i]
        else:
            d[arr[i]] = i


print("Two Sum | Test 1: ", two_sum([1,2,5,7],9))
print("Two Sum | Test 2: ", two_sum([2,7,11,15],9))