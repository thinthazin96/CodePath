
    
arr = sorted([[1,4], [2,5], [7,9]])

new_arr = []

# for i in range(len(arr)):
#     print(len(arr[i]))

start = 0
end = len(arr)
for i in range(len(arr)): #arr[0]
    print(arr[i])
    for j in range(len(arr[i])-1): #arr[0][0]
        # print(arr[i][j])
        if arr[i][len(arr[i])-1] >  arr[i][j]: #arr[0][1] > arr[1][0]
            break
    new_arr.append(min(arr[i]))

print(new_arr)
    
    
    





                