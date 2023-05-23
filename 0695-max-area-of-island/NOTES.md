1. Representing a matrix: The problem is shown a 2D Grid. Each cell in the array is either water (0) or land (1)
2. Preprocessing: converting values, adding up totals, or pulling out other important information?????
3. Visited cells: create a separate array to keep track of the cells that are already visited
4. Variable for Max Area
5. Rows and Colums Variables: Rows = len(grid) - 1, Cols = len(grid[0]) - 1
6. Boundaries/Edge cases: (r: 0, c: 0), (r: len - 1, c: 0), (r: 0, c: len - 1), (r: len -1, c: len -1). We can assume all four edges of the grid are surrounded by water.
7.  Grid Constraints: Only horizontal and vertical movement
8.  Direction Arrays: Use a helper function for this part and use Boundaries/Edge cases inside the helper function, if it allows you to. Mark the cell as visited. Apply the helper function for every direction.
9.  Connected Components: find and count the number of connected components
10.  Matrix Connectivity:Figure out if all the cells in the matrix are connected or how many different parts are connected. Consider using DFS or BFS to see how cells are linked.
11.  DFS: we can go as deep as possible and travel back up to move different directions