'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true

Input: s = "anagram", t = "nagaram"
Output: true

Edge Case: 
what if the length of the strings are not the same?

Understand: Two input strings and output has to be bool.
Match: dictionary
Planning: 
1) Create dictionary for each string to track the frequency of the letters
2) Check if the frequency of the letters in both strings are the same.
3) if all the same, return true
4) else return false.
'''
def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    dicS = {}
    dicT = {}
    for i in s:
        if i in dicS:
            dicS[i] += 1
        else:
            dicS[i] = 1
        
    for j in t:
        if j in dicT:
            dicT[j] += 1
        else:
            dicT[j] = 1
        
    for key, val in dicS.items():
        if key in dicT:    
         if val != dicT[key]:
            return False
        else:
            return False
    return True

# print(validAnagram("anagram", "nagaram"))
print(validAnagram("rat", "cat"))