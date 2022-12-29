'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Edge Case: What if both of the array is empty?
what is len of nums2 bigger than nums1?
Understand: two parameter for input, output is nums1 array(inplace order) the non-decreasing order of nums1 + num2 array.
Match:
Planning: 
1) add the len of nums1 + nums2.
2) loop throught the nums1.
3) if there is 0 in the nums1, remove.
4) loop through the nums2, append them in nums1.
4) return the updated nums1 list.
'''

def merge(nums1,m,nums2,n):
    sum = m + n
    i = -1
    if m == 0:
        while m >= i:
            if nums1[i] == 0:
                nums1[i] = nums2[i]
            i += 1

    while sum >= i:
        if nums1[i] == 0:
            nums1[i] = nums2[i]
        else:break
        i -= 1
        
    nums1 = sorted(nums1)
    return nums1
    
# print(merge([1,2,3,0,0,0],3,[2,5,6],3))
# print(merge([1],1,[],0))
print(merge([0],0,[1],1))

    
