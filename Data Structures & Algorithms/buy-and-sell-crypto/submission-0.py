class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        lowestprice = prices[0]

        for i in range(len(prices)):
            price = prices[i]
            lowestprice = min(lowestprice, price)
            maxprofit = max(maxprofit, price-lowestprice)
        
        return maxprofit
