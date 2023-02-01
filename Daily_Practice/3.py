'''
Longest Substring Without Repeating Characters: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Time Complexity: O(N) because of Set.

This problem mainly adding and removing from the Set.
'''
def lengthOfLongestSubstring(s):
    subString = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in subString:
            subString.remove(s[l])
            l += 1
        
        subString.add(s[r])
        res = max(res, r - l + 1)
    return res

# print("Longest Substring Without Repeating Characters: Test 1 || ", lengthOfLongestSubstring("abcabcbb") == 3)
# print("Longest Substring Without Repeating Characters: Test 2 || ", lengthOfLongestSubstring("bbbbb") == 1)
print("Longest Substring Without Repeating Characters: Test 3 || ", lengthOfLongestSubstring("pwwkew") == 3)
