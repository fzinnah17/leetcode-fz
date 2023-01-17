class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        So, the most naive way to approach this would be to choose each element as a starting position using a for loop, then using another forloop, we iterate through and record the maximum profit.

This approach does the job, but it takes O(N^2) runtime.

This means that we will slide the window by one element when we move on to the next array.
1. two pointers: left, right
2. maxProfit
3. left > right: right += 1
    right > left: max= max (itself, right - left)
    left += 1

        """
        maxProfit = 0
        buy, sell = 0, 1
        
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, (prices[sell] - prices[buy]))
            else:
                buy = sell
            sell += 1
        return maxProfit

                
            
        