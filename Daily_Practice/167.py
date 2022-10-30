'''
Two Sum II
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
def two_pointer_II(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        elif sum == target:
            return [left+1, right+1]

print("Test 1 || ", two_pointer_II([2,7,11,15], 9) == [1, 2])
print("Test 2 || ", two_pointer_II([2,3,4], 6) == [1, 3])
print("Test 3 || ", two_pointer_II([-1,0], -1) == [1,2])