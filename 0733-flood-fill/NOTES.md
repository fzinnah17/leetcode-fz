1. Representing a matrix: 2D array
2. Preprocessing: converting values, adding up totals, or pulling out important information????
3. Visited Cells: set() -> separate visited array
4. Rows and Colums Variables: Rows = len(grid) - 1 Cols = len(grid[0]) - 1
5. Boundaries/Edge cases: (r: 0, c: 0), (r: 0, c: len - 1), (r: len - 1, c : 0), and (r : len - 1, c: len - 1)
6. Grid Constraints and Traversal of the matrix: (vertically and horizontally) not diagonally
7. Direction Arrays: helper function
8. DFS: As we can go as deep as possible and when we reach the base case, we will go back up, but for each deep cell we will be checking the directions using the helper function