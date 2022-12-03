class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        output = 0
        visited = set()
        Rows = len(grid) - 1
        Cols = len(grid[0]) - 1 
        def helper(row, col):
            if (row < 0 or col < 0 or
                row > Rows or col > Cols or
                (row, col) in visited or grid[row][col] == '0'
               ):
                return
            visited.add((row,col))
            
            helper(row - 1,col)
            helper(row + 1, col)
            helper(row, col - 1)
            helper(row, col + 1) 
            # it's working
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if grid[row][col] == "1" and (row, col) not in visited:
                    helper(row, col)
                    output += 1
        return output
            
                
            
        