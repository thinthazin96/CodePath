'''
739. Daily Temperatures

Time Complexity = O(n)

'''
def dailyTemperatures(temperatures):

    stack = []                            # store pair:[temp, index]
    res = [0] * len(temperatures)          #get the same length as given list and set 0 if case of no future day

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]: #as long as the stack is not empty and current temp > than the top element -> stack(temperature, index): stack[-1][0]
            stackT, stackInd = stack.pop() #pop pair:[temp, index]
            res[stackInd] = (i - stackInd) #diff is the distance of index and store at that index position
        stack.append((t, i))
    return res

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
