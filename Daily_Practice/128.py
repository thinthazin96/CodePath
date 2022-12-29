'''
128. Longest Consecutive Sequence

Time Complexity = O(N)
'''


def longestConsecutive(nums):
  numSet = set(nums)  #to get O(N) time
  longest = 0

  for i in nums:
    if (i - 1) not in numSet:  #check the integer is the start of the sequence
      length = 1
      while (
          i +
          length) in numSet:  #check the integer sequence are in the input list
        length += 1  #Increase the length, if it has sequence
      longest = max(longest, length)  #get maximum length

  return longest


print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9)
print(longestConsecutive([100, 4, 200, 1, 3, 2]) == 4)
