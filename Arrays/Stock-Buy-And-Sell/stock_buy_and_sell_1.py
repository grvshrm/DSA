def maxProfit(prices: list, n: int) -> int: 
# Complexity : Time - O(n), Space - O(1)
    profit = 0
    mini = prices[0]
    for i in range(1, n):
        cost = prices[i] - mini
        profit = max(profit, cost)
        mini = min(mini, prices[i])
    return profit 

if __name__ == '__main__': 
	price = [7, 1, 5, 3, 6, 4] 
	n = len(price) 
	print(maxProfit(price, n))