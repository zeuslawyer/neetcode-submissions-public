class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        if len(prices) <= 1: return maxprofit

        lowpriceIdx = 0

        for i in range(1,len(prices)):
            price = prices[i]
            if price < prices[lowpriceIdx]: lowpriceIdx = i

            profit = prices[i] - prices[lowpriceIdx]
            maxprofit = max(maxprofit, profit)
        
        return maxprofit

