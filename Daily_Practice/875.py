'''
875. Koko Eating Bananas

Time Complexity: O(max(logm))
'''
def minEatingSpeed(piles, h):
    l = 1                
    r = max(piles)
    ans = max(piles)

    while l <= r:
        k = (l + r)//2

        totalTime = 0
        for p in piles:
            totalTime += int(p / k)

        if totalTime < h:
            ans = min(ans, k)
            r = k - 1

        else:
            l = k + 1
    return ans

print(minEatingSpeed([3,6,7,11], 8))
