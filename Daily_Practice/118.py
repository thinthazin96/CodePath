def generate(numRows):
    pascal = [[1]]
    if numRows == 0:            #if the input is 0, return empty list.
        return []
    
    for i in range(numRows - 1): 
        res = [1]
        for num in range(len(pascal[i])-1):
            res.append(pascal[i][num] + pascal[i][num+1])
        res.append(1)
        pascal.append(res)
        
    return pascal

print(generate(5))