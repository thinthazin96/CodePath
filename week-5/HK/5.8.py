'''
Subsequence Removal:

Given an array of positive integers, find the minimum length ascending subsequence such that after removing this subsequence from the array, the reamining array contains only unique integers. 
Only one subsequence will have the minimum length(no ties). 
If there is no such subsequence, return[-1]. 

Input: [2, 1, 3, 1, 4, 1, 3]
Output: [1, 1, 3]
'''
def findSubsequence(arr):
    arr.sort()
    ans = []
    hash = {}
    
    for i in range(0, len(arr)):
        if arr[i] not in hash:
            hash[arr[i]] = 1
        else:
            ans.append(arr[i])
            if arr[i] < ans[-1]:
                print(arr[i])
                print(ans)
                return [-1]
    
    if ans != None:
        return ans
    else:
        return [-1]