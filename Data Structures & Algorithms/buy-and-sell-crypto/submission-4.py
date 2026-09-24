class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:  return 0

        # # DP
        # maxprofit = 0
        # lowestprice = prices[0]

        # for i in range(len(prices)):
        #     price = prices[i]
        #     lowestprice = min(lowestprice, price)
        #     maxprofit = max(maxprofit, price-lowestprice)
        
        # return maxprofit

        # two pointer:

        minprice = prices[0]
        maxprofit = 0

        buyday, sellday = 0, 1

        # start from position 1
        for i in range( 1, len(prices)):
            if prices[buyday] < prices[sellday]:
                profit = prices[sellday] - prices[buyday]
                maxprofit = max(maxprofit, profit)
            else:
                buyday = sellday
            sellday+=1
        return maxprofit
            

