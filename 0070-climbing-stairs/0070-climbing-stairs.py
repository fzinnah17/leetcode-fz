from functools import lru_cache
class Solution(object):
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        """
        Psuedocode:
        1. Identify the Recursive Function: F(n - 1) + F(n - 2) We can climb the 'n' stairs by taking one or two steps at a time. So, if we're on step i right now, the only places we could go in one iteration are steps i + 1 (if we take one step) and i + 2 (if we take two steps).

This means that if we are now on step n, our final destination, we could only have arrived there in one of two ways:
From step n - 1, having gone up 1 step to n
From step n - 2, having gone up 2 steps to n

This shows that the number of ways to get to step n is dependent on the number of ways to get to step n - 1 and the number of ways to get to step n - 2. Because both of the previous options are valid, the number of ways to n is the sum of the two. So we have the following relationship, which is formally known as a recurrence relation: ways(n) = ways(n - 1) + ways(n - 2)
        2. Define a Memoization Table: {}
        3. Implement the Base Case(s):
                a. if n == 1: return 1 -> 1 step
                b. if n == 2: 1 step + 1 step , 2 steps
                     n - 2 : (n - 1) + (n - 1) , (n - 2) = 2 - 2 = 0
                            2 * (n - 1), (n - n)
        4. Check the Memoization Table if the steps are already store. If so, then return it.
        5. Perform Recursive Calls:
                a. if n > 2: Recursive Function
                            n == 3 -> 1 step + 1 step + 1 step, 2 steps + 1 step, 1 step + 2 steps
                                     (n - 1) + (n - 1) + (n - 1), (n - 2) + (n - 1), (n - 1) + (n - 2)
        6. Cache and Return the Result of the recursive call
        TC: O(n) SC: O(n)
        """
        memoTable = {}
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n > 2:
            #recursive function I am not sure because n * (n - 1) doesn't give distinct results
            memoTable[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return memoTable[n]
        
        if n in memoTable:
            return memoTable[n]