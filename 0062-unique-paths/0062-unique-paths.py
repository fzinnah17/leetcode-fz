class Solution(object):
    @lru_cache()
    def uniquePaths(self, m, n):
        """
        1. Identify the Recursive Function:
        2. Define a Memoization Table: {} I am trying to save the paths that has already been visited earlier so that path is not traversed again.
        3. Implement the Base Case(s):
                a. if m = 2 and n = 2:
                    return 2 (as there are 2 ways to reach the star)
                b. initial position: grid[0][0] return 1
                c. when it reaches the destination: grid[m-1][n-1] return 1
        4. Check the Memoization Table: If a cached result exists, return it immediately.
        5. Perform Recursive Calls with the the Recursive Function: there's only choices of going down and right only. So does it mean we add up the previous two calls?
        6. Cache and Return the Result: Store the computed result in the memoization table for future use.
        TC: O(m * n) because for each position (m, n), we make two recursive calls: one for (m - 1, n) and one for (m, n - 1).
        SC: O(m + n) for the memoTable
        """
        memoTable = {}
        if m == 1 and n == 1:
            return 1
        rowPath, colPath = 0, 0
        if m > 1:
            rowPath = self.uniquePaths(m-1, n)
        if n > 1:
            colPath = self.uniquePaths(m, n -1)

        memoTable[(m,n)] = rowPath + colPath
        return memoTable[(m,n)]
        if (m,n) in memoTable:
            return memoTable[(m,n)]
        
        
        