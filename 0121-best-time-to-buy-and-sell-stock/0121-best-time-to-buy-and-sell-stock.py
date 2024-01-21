class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Input: prices = [7,1,5,3,6,4]
                         | r 
        curr = r - l
        maxprofit = max(curr, maxprofit)
        
        Pesudocode for sliding window approach:
        1. we have variable to return and two pointers for the sliding window
        2. as we are iterating over the given array,
          a. we check thedifference between the stock prices of the days our pointers are at
          b. if left > right:
              i. shift our left pointer to the eight as we won't be earning any profit
          c. we will move our right pointer regardless of left < right or left > right
          d. update the maximum profit
        3. return the maximum profit
        """
        maxProfit = 0
        
        l, r = 0, 0
        
        while r < len(prices):
          curr = prices[r] - prices[l]
          if prices[l] > prices[r]:
            l = r
          r += 1
          maxProfit = max(maxProfit, curr)
        return maxProfit
          