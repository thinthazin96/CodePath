'''
704. Binary Search

Time Complexity: O(log n)
'''
def BinarySearch(nums, target):
    start = 0
    end = len(nums)
    while start < end:                  #Run as long as the start < end.
        middle_num = (start + end) // 2 #get middle number
        if nums[middle_num] > target:   #if middle value > target, go to left side
            end = middle_num
        elif nums[middle_num] < target: #if middle vlaue < target, go to right side
            start = middle_num + 1
        else:
            return middle_num           #if middle value == target, return its index
    return -1                           #if the target value is not in the list, return -1.


# print(BinarySearch([-1,0,3,5,9,12], 9))
print(BinarySearch([-1,0,3,5,9,12], 2))
            
