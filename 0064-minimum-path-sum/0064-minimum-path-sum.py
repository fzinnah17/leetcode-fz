class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        # Fill the first row and column with cumulative sums
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
            
        # Fill the rest of the grid with the minimum sum to each cell
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        # Return the minimum sum to the bottom-right cell
        return grid[-1][-1]
