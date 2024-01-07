class Solution(object):
    @lru_cache()
    def uniquePaths(self, m, n):
        """

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
        
        
        