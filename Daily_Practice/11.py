'''
Container With Most Water: https://leetcode.com/problems/container-with-most-water/

Time Complexity:
'''
def maxArea(height):

    #Brute Force: Time Complexity: O(N^2) 

    # res = 0

    # for i in range(len(height)):
    #     for j in range(i+1, len(height)):
    #         area = (j - i) * min(height[i], height[j]) # area = width * height
    #         res = max(res, area)  # keep track of the max area

    # return res

    #-------Two Pointer Method: Time Complexity: O(N)--------

    max_area = 0
    l = 0
    r = len(height) - 1
    
    while l < r:
        #It's only beneficial to move short line than the long line. that's why min function is called.
        area = (r - l) * min(height[l], height[r]) # area = width * height
        max_area = max(max_area, area)  # keep track of the max area 

        if height[l] < height[r]:
            l += 1
        else:   #if the left > right or left == right:
            r -= 1

    return max_area

print("Test 1 || ", maxArea([1,8,6,2,5,4,8,3,7]) == 49)
