class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: prices = [7,1,5,3,6,4]
                         | r 
        curr = r - l
        maxprofit = max(curr, maxprofit)
        """
        maxProfit = 0
        
        l, r = 0, 1
        
        while r < len(prices):
          curr = prices[r] - prices[l]
          if prices[l] > prices[r]:
            l = r
          r += 1
          maxProfit = max(maxProfit, curr)
        return maxProfit
          