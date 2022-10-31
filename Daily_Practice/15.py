'''
Three Sum: https://leetcode.com/problems/3sum/
'''
def threeSum(nums):
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]: # To avoid duplicates
                twoSumII(nums, i, res)
        return res
                
            
def twoSumII(nums, i, res):
    left = i + 1
    right = len(nums) - 1
    
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum > 0:
            right -= 1
        elif sum < 0:
            left += 1
        else:
            res.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left - 1]: # To avoid duplicate in the res.
                left += 1

print("Test 1 || ", threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
print("Test 2 || ", threeSum([0,1,1]) == [])
print("Test 3 || ", threeSum([0,0,0]) == [[0,0,0]])