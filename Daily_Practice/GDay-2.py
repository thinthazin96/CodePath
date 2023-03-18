'''
"ACTNG", "AT", "CG", 

input: string, output: string

'''
def DNA(s):

    ans = ""
    for i in s:
        if i == "A":
            ans = ans + "T"
        elif i == "C":
            ans = ans + "G"
        elif i == "G":
            ans = ans + "C"
        elif i == "T":
            ans = ans + "A"

    return ans

print(DNA("ATTAG"))

'''
input: integer, output: 

input : 376006
output : 

Given: 0 -9 with 
'''


# def calculator():

# s = ord("O") - ord("A")
# print(s)

def test(strs):

    if "cd" in strs:
        return True

strs = "abcd"
print(test(strs))