'''
Group Anagrams: https://leetcode.com/problems/group-anagrams/

Time Complexity: O(m * n * 26) -> m = length of the original list, n = average length of a string in the list, 
                0(m * n)
'''
import collections

def groupAnagrams(strs):
    res = collections.defaultdict(list)   #Defaultdict() doesn't give key error on non-existence key.

    for s in strs:                  #loop through each element in list
        count = [0] * 26            #reserve 26 spot for a -z
        for c in s:                 #loop each character of a string in the list
            count[ord(c) - ord("a")] += 1   #track frequency of each character | Ascii Hax value increase as it go down
        res[tuple(count)].append(s)         #Take frequency as a key and string value as a value     
    return res.values()             #Return all the values of the dictionary

'''
Python syntax:
dictionary doesn't take list as a key but it does take tuple as a key.
Key Error occurs if a key doesn't exist in the dictionary.
'''

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))