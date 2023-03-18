def oneEditAway(s1, s2):
        
        if len(s1) == len(s2): # pale, bale
            return replace(s1, s2)

        elif len(s1) > len(s2): #pales, pale
            return insert(s1, s2)

        elif len(s1) < len(s2): # ple, pale
            return remove(s1, s2)    
        
        else:
            return False


def replace(s1, s2):
    count, p1, p2 = 0, 0, 0
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1
            p2 += 1
        else:
            p1 += 1
            p2 += 1
            count += 1
            if count > 1:
                return False
    return True

def insert(s1, s2):
    count, p1, p2 = 0, 0, 0
    if len(s1) - len(s2) > 1:
        return False
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1     
            p2 += 1          
        else:
            p1 += 1
            # p2 += 1
            count += 1
            if count > 1:
                return False
    return True

def remove(s1, s2):
    if not s2:          #if s2 is empty, return false
        return False
    
    if len(s2) - len(s1) > 1:
        return False
    count, p1, p2 = 0, 0, 0
    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] == s2[p2]:
            p1 += 1     
            p2 += 1          
        else:
            # p1 += 1
            p2 += 1
            count += 1
            if count > 1:
                return False
    return True

print(oneEditAway("pale", "ple"))
print(oneEditAway("pales", "pale"))
print(oneEditAway("pale", "bale"))
print(oneEditAway("pale", "bake"))

# print(oneEditAway("pale", "bae"))
# print(oneEditAway("aple", "apple"))
print(oneEditAway("doghouse", "dog"))
# print(oneEditAway("dog", "doghouse"))