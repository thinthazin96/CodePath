'''
853. Car Fleet

zip() func pair two list.
'''
def carFleet(target, position, speed):
    pair = [(p, s) for p, s in zip(position, speed)]
    stack = []
    pair.sort(reverse=True)                              #sort the list and reverse the list [R to L bcz the speed will change before reaching to destination]
    
    for p, s in pair:                  
        stack.append((target - p)/ s)                   # Calculate the time to reach the target and push it into stack
        if len(stack) >= 2 and stack[-1] <= stack[-2]:  # if the stack has more than one element in it && top element speed is less than its previous element speed, pop the top element
            stack.pop()

        #if the stack has only one element in it, don't care
    return len(stack)

print(carFleet(12,[10,8,0,5,3],[2,4,1,1,3]))

     