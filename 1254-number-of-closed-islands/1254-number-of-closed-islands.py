class Solution(object):
    def closedIsland(self, grid):
        """
Time complexity is O(n * m), where n is the number of rows and m is the number of columns in the grid. This is because, even in the worst case, we might only have to go to each grid cell once.

Space complexity is also O(n * m) in the worst case. This is because we use a set called "visited" to keep track of which cells have been used. This set could hold all of the cells in the grid. Also, recursive calls to the helper function can use space on the recursion stack, which can add to the space complexity. But if we ignore the space used by the input grid and only look at the extra space the algorithm needs, the space complexity is O(n + m), because we use a separate set for visited cells.
        """
        Rows = len(grid) - 1
        Cols = len(grid[0]) - 1
        visited = set()
        result = 0
        def helper(row,col):
            if(
            row < 0
            or col < 0
            or row > Rows
            or col > Cols):
                return 0
            if grid[row][col] == 1 or (row,col) in visited: #1 is water
                return 1
            visited.add((row,col))
            return min(
            helper(row + 1, col),
            helper(row - 1, col),
            helper(row, col + 1),
            helper(row, col - 1))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and (r,c) not in visited:
                    result += helper(r,c)
        return result
        
        