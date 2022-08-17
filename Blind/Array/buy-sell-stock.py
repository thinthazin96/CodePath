"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

U - input is a list of array and output is integer which is maximum profit.

M - Two pointer Method

TODO : Planning
1) set left pointer at the beginning of the list and the right pointer which is one pointer ahead of the left pointer.
2) set max_profit to track the maximum profit
3) loop as long as right pointer is less than the length of the list.
    a) find the current_profit by prices[right] - prices[left]
    b) if the left pointer's value is less than the right pointer's value, find the max profit
    c) else move the left pointer and right pointer up.
"""
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

print("Best Time to Buy and Sell Stock || Test 1: ", maxProfit([7,1,5,3,6,4]) == 5)
print("Best Time to Buy and Sell Stock || Test 2: ", maxProfit([7,6,4,3,1]) == 0)