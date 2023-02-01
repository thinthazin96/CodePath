'''
Best Tim to Buy and Sell Stock: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

def maxProfit(prices):
    left = 0
    right = 1
    max_profit = 0

    while right < len(prices):
        current_profit = prices[right] - prices[left]
        
        if prices[left] < prices[right]:
            max_profit = max(current_profit, max_profit)
        else:
            left = right
        right += 1

    return max_profit

print("Best Time to Buy and Sell Stock: Test 1 || ", maxProfit([7,1,5,3,6,4]) == 5)
print("Best Time to Buy and Sell Stock: Test 2 || ", maxProfit([7,6,4,3,1]) == 0)

#=====================================================================================

def maxProfit(prices):
    diff = 0
    left = 0
    right = 0

    while right < len(prices):
        cur_diff = prices[right] - prices[left]
        
        if cur_diff > diff:
            diff = cur_diff

        if prices[right] <= prices[left]:
            left = right
            right += 1
        else:
            right += 1
    return diff

print(maxProfit([7,1,5,3,6,4]))