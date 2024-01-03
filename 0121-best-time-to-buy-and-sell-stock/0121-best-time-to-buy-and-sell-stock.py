class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of minimum purchase price and maximum profit
        min_purchase = float("inf")  # Set to positive infinity
        max_profit = 0
        
        # Iterate through the prices list
        for price in prices:
            # Update the minimum purchase price if the current price is lower
            min_purchase = min(min_purchase, price)
            
            # Calculate the potential profit by selling at the current price
            potential_profit = price - min_purchase
            
            # Update the maximum profit if the potential profit is greater
            max_profit = max(max_profit, potential_profit)
            
        # Return the maximum profit obtained
        return max_profit
