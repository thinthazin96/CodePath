def firstUniqChar(s):
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for key,value in d.items():
            if value != 1:
                continue
            else:
                for i in range(len(s)):
                    if s[i] == key:
                        return i 
            
        return -1

print(firstUniqChar("loveleetcode"))