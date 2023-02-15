'''
1200: Minimum Absolute Difference
'''
def minimumAbsDifference(arr):
    '''
    1. create min_diff to keep track of minimum difference.
    2. create dictionary to store differences as key and pair value as value -> [(value, value)].
    3. sort the list and iterate throught the sorted list.
    4. find current diff of current index and the other and add them into dictionary.
    5. update the min_diff if current diff > min_diff.
    6. iterate through the hashmap.
        i. if the min_diff == key match, return the list of value. 
    '''

    d = {}
    sorted_arr = sorted(arr)
    min_diff = sorted_arr[-1] - sorted_arr[-2]

    for i in range(len(sorted_arr)):
        for j in range(i+1, len(sorted_arr)):
            curr_diff = sorted_arr[j] - sorted_arr[i]
            if curr_diff not in d:
                d[curr_diff] = [[sorted_arr[i], sorted_arr[j]]]
            else:
                d[curr_diff].append([sorted_arr[i], sorted_arr[j]])
            
            min_diff = min(curr_diff, min_diff)

    for key, value in d.items():
        if min_diff == key:
            return value

# print(minimumAbsDifference([4,2,1,3]))
print(minimumAbsDifference([40,11,26,27,-20]))