'''
Product of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/

Time Complexity: O(n)
'''

def productExceptSelf(nums):
    answer = [1] * len(nums)    # create array same length as input array by reserving 1
    
    prefix = 1                  # choose 1 value to neutralize
    for i in range(len(nums)):
        answer[i] = prefix      # whatever prefix value will update the current new array value
        prefix *= nums[i]       # update the prefix value

    postfix = 1
    for i in range(len(nums)-1, -1, -1): #loop in reverse order
        answer[i] *= postfix            #Overwrite the current value of new array by multiplying it with the postfix    
        postfix *= nums[i]              #update the postfix value

    return answer

print(productExceptSelf([1,2,3,4]))