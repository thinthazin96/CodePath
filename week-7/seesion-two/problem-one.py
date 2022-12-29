def first_subarray_with_sum(nums, target):
    l = len(nums)

    window_sum, low, high = 0, 0, 0

#   while low < l: # O(n)
    while window_sum < target and high < l:
        window_sum += nums[high]
        high += 1

    if window_sum == target:
        return nums[low:high]

    while window_sum > target:
        window_sum -= nums[low]
        low += 1

    # After adding the outer while loop, I can remove this check
    #if window_sum == target:
    #  return nums[low:high]

    if window_sum < target and low == 0 and high == l:
        return []

#   return []

def main():
  tests = [
    # { 'input': { 'nums': [1,2,3], 'target': 3 }, 'output': [1,2] },
    # { 'input': { 'nums': [1,2,3], 'target': 5 }, 'output': [2,3] },
    # { 'input': { 'nums': [1], 'target': 1 }, 'output': [1] },
    # { 'input': { 'nums': [], 'target': 0 }, 'output': [] },
    # { 'input': { 'nums': [1,2,3], 'target': 7 }, 'output': [] },
    # { 'input': { 'nums': [2,6,0,9,7,3,1,4,1,10], 'target': 15 }, 'output': [6,0,9] },
    { 'input': { 'nums': [0,5,7,1,4,7,6,1,4,1,10], 'target': 15 }, 'output': [4,1,10] },
    # { 'input': { 'nums': [0,5,7,1,4,7,6,1,4,1,10], 'target': 8 },  'output': [7,1] },
  ]
  
  for i in range(len(tests)):
    print(f'Test {i+1}:', first_subarray_with_sum(tests[i]['input']['nums'], tests[i]['input']['target']) == tests[i]['output'])

main()