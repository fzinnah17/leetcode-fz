class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        Rows = len(grid)
        Cols = len(grid[0])
        visited = set()

        # Define a recursive depth-first search (DFS) function.
        def dfs(r, c, pointer):
            # Check if we've matched the entire word.
            if len(word) == pointer:
                return True
            # Check for boundary conditions and visited cells.
            if (r < 0 or c < 0
                or r >= Rows or c >= Cols
                or (r, c) in visited
                or grid[r][c] != word[pointer]):
                return

            visited.add((r, c))
            # Recursively search in all four directions.
            res = (dfs(r + 1, c, pointer + 1) or
                   dfs(r - 1, c, pointer + 1) or
                   dfs(r, c + 1, pointer + 1) or
                   dfs(r, c - 1, pointer + 1))
            visited.remove((r, c))
            return res

        # Iterate through the grid to find the starting point for the word.
        for row in range(Rows):
            for col in range(Cols):
                if grid[row][col] == word[0]:
                    # Start DFS from this point.
                    if dfs(row, col, 0):
                        return True
        # If we didn't find the word starting from any point, return False.
        return False
