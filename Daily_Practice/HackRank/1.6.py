'''
String Compression:
'''
#Two Pointer with count approach
# def Compression(s):
    
#     count, l, r = 0, 0, 0
#     ans = ""
#     while r < len(s):
#         if s[l] == s[r]:
#             ans += s[l]
#             count += 1
#             r += 1

#         else:
#             ans += str(count)
#             count = 0
#             l = r
#             ans += s[l]
#             count += 1
#             r += 1
#     ans += str(count)
#     return ans

def Compression(s):

    l, r = 0, 0
    big_list = []
    small_list = []
    while r < len(s):
        
        if s[l] == s[r]:
            small_list.append(s[l])
            r += 1
        
        else:
            big_list.append(small_list)
            small_list = [] 
            l = r
            small_list.append(s[l])
            r += 1

    big_list.append(small_list)

    for i in range(len(big_list)):
        big_list[i] = big_list[i][0] + str(len(big_list[i]))
    
    return "".join(big_list)

    #------Leetcode solution------- Not inplace
    # ans = []
    # for i in range(len(big_list)):
    #     if len(big_list[i]) == 1:
    #         ans.append(big_list[i][0])
    #     else:
    #         ans.append(big_list[i][0])
    #         ans.append(str(len(big_list[i])))
    # print(ans)
    # return len(ans)
print(Compression(['a', 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'a', 'a', 'a']))
print(Compression(["a","a","b","b","c","c","c"]))
print(Compression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(Compression(["a"]))

