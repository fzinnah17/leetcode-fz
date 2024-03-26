class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Break into base case where n = 1 return True
        if n == 1:
            return True

        # Break into base case where n = 0 or n is no longer a whole number when divided by 4 return False
        if n == 0 or n % 4 != 0:
            return False

        # Return the recursive function n/4 
        return self.isPowerOfFour(n/4)
        