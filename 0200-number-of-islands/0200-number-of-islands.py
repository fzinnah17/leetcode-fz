class Solution(object):
    def numIslands(self, grid):
        output = 0
        numRows = len(grid)
        numCols = len(grid[0])
        visited = set()
        def dfs(r,c):
            if(
                r < 0 or c < 0 or
                r >= numRows or c >= numCols or
                grid[r][c] == '0' or (r,c) in visited
            ):
                return
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for rows in range(numRows):
            for cols in range(numCols):
                if ((rows,cols)) not in visited and grid[rows][cols] == "1":
                    dfs(rows,cols)
                    output += 1
        return output
    #TC: O(n + m) SC: O(n * m)
        