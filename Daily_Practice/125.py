'''
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

'''
def valid_palindrome(s):
    
    l = 0
    r = len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue
        if not s[r].isalnum():
            r -= 1
            continue
        if s[l].lower() != s[r].lower():
            return False
        else:
            l += 1
            r -= 1
        
    return True

print("Test 1 || ", valid_palindrome("A man, a plan, a canal: Panama") == True)
print("Test 2 || ", valid_palindrome("race a car") == False)
