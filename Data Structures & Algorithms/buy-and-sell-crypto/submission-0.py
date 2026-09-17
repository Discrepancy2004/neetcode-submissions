class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        n = len(prices)
        profit = 0
        maxProfit = 0
        while(r<n):
            if prices[r] - prices[l] > 0:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit,profit)
                

            else:
                l = r
            
            r = r + 1

        return maxProfit
            