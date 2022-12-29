'''
Subsequence Removal:

Given an array of positive integers, find the minimum length ascending subsequence such that after removing this subsequence from the array, the reamining array contains only unique integers. 
Only one subsequence will have the minimum length(no ties). 
If there is no such subsequence, return[-1]. 

Input: [2, 1, 3, 1, 4, 1, 3]
Output: subsequence: [1, 1, 3]

Planning:
1. sort the array in ascending order.
2. create empty list [ans] to store the subsequence of the input_list.
3. create empty list [hash] to store the remaining of the input_list after removing the subsequences.
4. store the first apperance of the number in hash.
5. store the second or more apperance of the number in ans.
6. if the ans list is empty, return -1 because it means the input_list has no subsequence.
'''
def findSubsequence(arr):
    arr.sort()
    ans = []                        #store the subsequence in the array
    hash = []                       #remain array afer removing subsequence from input_list
    
    #i = 3 -> 3
    for i in range(0, len(arr)):    #loop through the array
        if arr[i] not in hash:      #if the element is not in the dictionary
            hash.append(arr[i])        #set the value to 1. {1: 1, 3: 1}
        else:                       #if the element already exists in the dictionary
            ans.append(arr[i])      #append that element in the list.
            # if arr[i] < ans[-1]:    #if current value is less than the last element in the array.
            #     print(arr[i])       #
            #     print(ans)
            #     return [-1]
    
    if ans != []:                 #if the ans list is not empty, return ans
        return ans                  #subsequence
    else:                           #else return -1
        return [-1]

print(f"Test 1:" , findSubsequence([2, 1, 3, 1, 4, 1, 3]) == [1, 1, 3])
# print(findSubsequence([3, 2, 2, 1, 1]))
print(f"Test 2:" , findSubsequence([3, 2, 2, 1, 1]) == [1, 2])
print(f"Test 3:" , findSubsequence([1, 1, 1, 3]) == [1, 1])
# print(findSubsequence([1,2,3]))