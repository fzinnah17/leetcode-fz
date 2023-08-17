class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for n in range(1, len(prices)):
            if prices[n] - prices[n-1] > 0:
                profit += prices[n] - prices[n-1]
        return profit
        