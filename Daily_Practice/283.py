'''
U - input:list type, output: list type, in-place order.
M - Two Pointer method
P 
1) set the left pointer at the beginning and right pointer next to it.
2) loop through the list, if the right pointer is non-zero, swap out.
3) increment the left and right pointer.

'''
def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right]:              #if the number is non-zero
            temp = nums[left]        #Store the current left value in temp
            nums[left] = nums[right] #store current right value in left which is empty now.
            nums[right] = temp       #store the temp value in right which is empty now.
            left += 1                #increment the left count.
    return nums

print(moveZeroes([0, 1, 0, 3, 12]))

