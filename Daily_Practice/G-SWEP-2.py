
def solution(arr):
    
    '''
    1. iterate throught the list and iterate again inside the string.
    2. create dictionary to take Index as Key and character as value.
    3. if the index doesn't exit in key, create it with value.
    4. if the index already exit append the value in value's list of the associated key.
    5. iterate through the dictionary and join each value list of index
    6. append all the value in a string and return the answer.
    '''
    d = {}
    res = ""
    for s in arr:
        for i in range(len(s)):
            if i not in d:
                d[i] = [s[i]]
            else:
                d[i] += s[i]
        
    for key,value in d.items():
        res += "".join(value)
    return res

print(solution(arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]))