class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        Base case: dp[n-1][m-1] = 0, dp[i][j] = 1 when there is a trap
        State/Subproblem: for each cell i, dp[i][j] = number of ways to go from (i,j) to (n-1, m-1)
        Transition/Formula: dp[i][j] = dp[i+1][j]+dp[i][j+1]
        Final problem: dp[0][0]
        """
        rows = len(grid)
        cols = len(grid[0])
        if grid[0][0] == 1 or grid[rows -1][cols - 1] == 1:
            return 0
        memoTable = {}
        
        def helper(r,c):
            if r >= rows or c >= cols or grid[r][c] == 1: #boundaries or found an obstacle in the destination cell(subproblem)
                return 0 #path
            if r == rows - 1 and c == cols - 1: #we found a path
                return 1 #path
            if (r,c) in memoTable:
                return memoTable[(r,c)] #already in the table :cache
            memoTable[(r,c)] = helper(r+1,c) + helper(r,c+1) #transition
            return memoTable[(r,c)] #return the table
        return helper(0,0)
        