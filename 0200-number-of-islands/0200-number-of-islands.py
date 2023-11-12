class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        numRows, numCols = len(grid), len(grid[0])
        
        def dfs(r,c):
            if (r < 0 or
               c < 0 or
               r >= numRows or
               c >= numCols or
                grid[r][c] == "0" or
               (r,c) in visited):
                return 
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for row in range(numRows):
            for col in range(numCols):
                if (row,col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        return islands
        