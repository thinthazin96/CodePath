'''
Two Sum: https://leetcode.com/problems/two-sum/
'''

def two_sum_I(numbers, target):

    d = {}
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement not in d:
            d[numbers[i]] = i
        else:
            return [d[complement], i]

print("Two Sum: Test 1 || ", two_sum_I([2,7,11,15], 9) == [0,1])
print("Two Sum: Test 2 || ", two_sum_I([3,2,4], 6) == [1,2])
print("Two Sum: Test 3 || ", two_sum_I([3,3], 6) == [0,1])