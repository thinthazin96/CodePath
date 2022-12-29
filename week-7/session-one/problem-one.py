'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Examples:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
'''
# def sort(arr):
#     leftPtr = 0
#     rightPtr = len(arr) - 1

#     while leftPtr < len(arr) - 1 and arr[leftPtr] < arr[leftPtr + 1]:
#         leftPtr = leftPtr + 1
    
#     if leftPtr == len(arr) - 1: #handle one element in the array edge case.
#         return 0

#     while rightPtr > 0 and arr[rightPtr] > arr[rightPtr - 1]:
#         rightPtr = rightPtr - 1

def shortest_subarray_removed(arr):
    if not arr: 
        return 0
    
    # 1. find the left pointer. loop from index 0, and find where an element is out-of-order
    left = 0
    right = len(arr) - 1

    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                          ^
    while left < len(arr) - 1 and arr[left] <= arr[left+1]:
        left += 1

    # 2. if in non-decreasing order -> return 0
    if left == len(arr) - 1:
        return 0
    
    # 3. find the right pointer. loop from index len(arr) - 1, and find where an element is out-of-order
    while right > 0 and arr[right] >= arr[right-1]:
        right -= 1

    # 4. compare arr[left-1] to arr[right], if arr[left-1] > arr[right] -> increase our window to include arr[left-1]

    i = 0
    j = right

    ans = len(arr) 
    
    # move i up to left because worst case we just keep the first i to left elements which are non-decreasing 

    # i = 0, j = 6
    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                        ^   ^
    #               i            j

    # i = 1, j = 6
    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                        ^   ^
    #                 i          j

    # 2, 6
    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                        ^   ^
    #                   i        j

    # 2, 7 -> updates min, min = 4
    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                        ^   ^
    #                   i          j

    # 3, 7
    # Input: arr = [1,2,3,8,10,4,2,3,5]
    #                        ^   ^
    #                     i        j
    
    while i <= left and j < len(arr):
        if arr[j] >= arr[i]:   # if we can narrow the window
            ans = min(ans, j - i - 1)
            i += 1    # increment i to narrow the window
        else:
            j += 1    # increment j to expand the window

    print(ans)
    return ans

print("Test 1: ", shortest_subarray_removed([1, 3, 2, 0, -1, 7, 10]) == 5)
print("Test 2: ", shortest_subarray_removed([1, 2, 5, 3, 7, 10, 9, 12]) == 5)