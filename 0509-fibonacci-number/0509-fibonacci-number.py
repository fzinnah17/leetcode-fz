class Solution(object):
    def fib(self, n):
        """
        1. Main recursive function: F(n) = F(n - 1) + F(n - 2)
        2. Define a Memoization Table: {} to store the cache results
        3. Base cases(terminates the recursion and provides a result):
                a. n = 0 -> return 0
                b. n = 1 -> return 1
                c. n = 2 -> return 1
        4. Check the Memoization Table: if the value is in table: return the cached value
        5. Perform Recursive Calls: perform the formula of the main recursive call for the conditions
                a. if n > 2:
                return F(n - 1) + F(n - 2)
        5. Cache and Return the Result: store it in the memoization table and return it
        """
        memoTable = {}
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            memoTable[n] = self.fib(n-1) + self.fib(n-2)
            return memoTable[n]
        if n in memoTable:
            return memoTable[n]
        #TC: O(n) because it depends on the number of function calls we make
        #SC: O(n) for creating a hash map.