class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()
        output = 0
        
        def dfs(r,c):
            if(r < 0 or c < 0 or r >= Rows or c >= Cols or (r,c) in visited or grid[r][c] == "0"):
                return
            visited.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)
                  
        for row in range(Rows):
            for col in range(Cols):
                if (row, col) not in visited and grid[row][col] == "1":
                    dfs(row, col)
                    output += 1
        return output
                
        