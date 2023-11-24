class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()
        
        def dfs(r, c, pointer):
            if len(word) == pointer:
                return True
            if(r < 0 or c < 0
              or r >= Rows or c >= Cols
              or (r,c) in visited
              or grid[r][c] != word[pointer]):
                return
            visited.add((r,c))
            res = (dfs(r + 1, c, pointer + 1) or
                  dfs(r - 1, c, pointer + 1) or
                  dfs(r, c + 1, pointer + 1) or
                  dfs(r, c- 1, pointer + 1))
            visited.remove((r,c))
            return res
        
        for row in range(Rows):
            for col in range(Cols):
                if grid[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False
                    
                    
                
        
        
        