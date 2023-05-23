class Solution(object):
    def maxAreaOfIsland(self, grid):
        """1. Representing a matrix: The problem is shown a 2D Grid. Each cell in the array is either water (0) or land (1)
2. Preprocessing: converting values, adding up totals, or pulling out other important information?????
3. Visited cells: create a separate array to keep track of the cells that are already visited
4. Variable for Max Area
5. Rows and Colums Variables: Rows = len(grid) - 1, Cols = len(grid[0]) - 1
6. Boundaries/Edge cases: (r: 0, c: 0), (r: len - 1, c: 0), (r: 0, c: len - 1), (r: len -1, c: len -1). We can assume all four edges of the grid are surrounded by water.
7.  Grid Constraints: Only horizontal and vertical movement
8.  Direction Arrays: Use a helper function for this part and use Boundaries/Edge cases inside the helper function, if it allows you to. Mark the cell as visited. Apply the helper function for every direction. 
9.  Connected Components: find and count the number of connected components
10.  Matrix Connectivity:Figure out if all the cells in the matrix are connected or how many different parts are connected. Consider using DFS or BFS to see how cells are linked.
11.  DFS: we can go as deep as possible and travel back up to move different directions"""
        visited = set()
        Rows = len(grid) - 1
        Cols = len(grid[0]) - 1
        maxArea = 0
        
        def helper(row, col):
            if (
                row < 0
                or col < 0
                or row > Rows
                or col > Cols
                or (row, col) in visited
                or grid[row][col] == 0
            ):
                return 0
            
            visited.add((row, col))
            area = 1
            area += helper(row + 1, col)
            area += helper(row - 1, col)
            area += helper(row, col + 1)
            area += helper(row, col - 1)
            return area

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited:
                    calculatedArea = helper(r, c)
                    maxArea = max(maxArea, calculatedArea)
        
        return maxArea
    # TC: O(m * n), where m and n are the dimensions of the matrix. This is because we potentially visit each cell in the matrix once. 
    # SC: O(m * n) in the worst-case scenario, when all of the land (1's) are in the grid. This is because, in the worst case, the recursion stack can contain up to m * n frames, one for each land cell. When a recursive call is made, a frame is added to the stack. When the maximum depth of the recursion is reached, we begin going backwards and popping frames off the stack. 
    #     O(m + n), however, if we disregard the space used by the input grid and only consider the extra space required by the algorithm. This includes the space occupied by the visited set, which can have at most m + n different cell coordinates (assuming no duplicates). The space used by the recursion stack is ignored in this space complexity analysis.


