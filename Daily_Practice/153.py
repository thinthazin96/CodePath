'''
153. Find Minimum in Rotated Sorted Array

Time Complexity: O(long n)
'''
def findMin(nums):
    l, r = 0, len(nums) - 1
    ans = nums[0]

    while l <= r:
        if nums[l] < nums[r]:
            ans = min(ans, nums[l])
            break

        m = (l + r) // 2
        ans = min(ans, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
        
    return ans

print(findMin([3,4,5,1,2]))
print(findMin([4,5,6,7,0,1,2]))
print(findMin([11,13,15,17]))


