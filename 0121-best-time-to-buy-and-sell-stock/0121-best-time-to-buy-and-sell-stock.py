class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      """
      7 1 5 3 6 4
      l
      r
      
      while loop r < len(arr) because it ensures that the right pointer (r) stays within the bounds of the array while expanding the window. This prevents index out of range errors and ensures that the window does not extend beyond the end of the array.
      if r < l: l == r, 7 should come to 1
      if r > l: r += 1, this movement should be done regardless, calculate the max
      compare the previous calculated max and with max()
      return whatever is the largest
      """
      
      l, r = 0, 0
      highest = 0
      
      while r < len(prices):
        curr = prices[r] - prices[l]
        if prices[r] < prices[l]:
          l = r
        r += 1
        highest = max(highest, curr)
      return highest