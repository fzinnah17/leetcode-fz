class Solution(object):
    def minPathSum(self, grid):
        """
brute force: every grid cell has two choices so f(i,j) = pathsum so far + min(f(i, j + 1), f(i+1,j))
        numRows = len(grid)
        numCols = len(grid[0])
        
        def dp(r,c):
            if (r >= numRows or c >= numCols):
                return float("inf")
            if (r == numRows - 1 and c == numCols - 1):
                return grid[r][c]
            
            return grid[r][c] + min(dp(r + 1,c), dp(r, c + 1))
        return dp(0,0)
DP:
    1. Variables: rows, cols, 2D list/grid for memoization
    2. Helper function: 
            a. boundaries
            b. if we reached the last cell of the grid/destination
            c. Now we are working in the memoTable:
                if the memoTable value is not -1:
                    we already computed the result so return that
                if the memoTable value == -1:
                    compute the memoTable path value = current cell value + min(right choice, bottom choice)
                return that memoTable path value
    3. return the helper function(0,0) as we are starting from the 0th cell
    TC: O(n * m) SC: O(n * m)
        """
        numRows = len(grid)
        numCols = len(grid[0])
        memoTable = [[-1 for _ in range(numCols)] for _ in range(numRows)]#2D list(lists of lists/create a 2D grid, rows represented as the outer lists and the columns as the inner lists) The -1s here serve as placeholders. They indicate that we have not yet computed a value for that position. -1 in our memoTable, it means we haven't solved that sub-problem yet, and so we need to compute it. If it's not -1, then we've already solved that sub-problem and can just return the stored result.
        
        def dp(r,c):
            if (r < 0 or c < 0 or r >= numRows or c >= numCols):
                return float("inf")
            if (r == numRows - 1 and c == numCols - 1):
                return grid[r][c]
            if memoTable[r][c] != -1:
                return memoTable[r][c]
            memoTable[r][c] = grid[r][c] + min(dp(r + 1,c), dp(r, c + 1))
            return memoTable[r][c]
        return dp(0,0)
        