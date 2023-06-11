class Solution(object):
    def integerReplacement(self, n):
        """
        TC: O(log n). This is because in each recursive call, the value of n is divided by 2 if it is even, or incremented/decremented by 1 if it is odd. This halving or increment/decrement operation reduces the value of n exponentially. Therefore, the number of recursive calls required to reach the base case (n = 1 or 2) is logarithmic in n 
        SC: O(n)
        """
        memoTable = {}
        memoTable[1] = 0
        memoTable[2] = 1
        if n in memoTable:
            return memoTable[n]
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n / 2)
        else:
            memoTable[n] = 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
            return memoTable[n]
            
        