class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        Pseudocode:
        1. Take a look at each cell. 
            A. If the cell value is same as sr and sc, then 
                change the value of it to the color value
                move 4 directionally
                    if 4 directions have the same value as 'sr' and 'sc', then make it the same color as the color
                    if any 4 directions value is not the same as sr and sc or perhaps '0', then don't change that color
        Return that modified matrix
        1. Representing a matrix: 2D array
2. Preprocessing: converting values, adding up totals, or pulling out important information????
3. Visited Cells: set() -> separate visited array
4. Rows and Colums Variables: Rows = len(grid) - 1 Cols = len(grid[0]) - 1
5. Boundaries/Edge cases: (r: 0, c: 0), (r: 0, c: len - 1), (r: len - 1, c : 0), and (r : len - 1, c: len - 1)
6. Grid Constraints and Traversal of the matrix: (vertically and horizontally) not diagonally
7. Direction Arrays: helper function
8. DFS: As we can go as deep as possible and when we reach the base case, we will go back up, but for each deep cell we will be checking the directions using the helper function
        """
        visited = set()
        Rows = len(image) - 1
        Cols = len(image[0]) - 1

        def helper(row, col, oldColor):
            if (
                row < 0
                or col < 0
                or row > Rows
                or col > Cols
                or image[row][col] != oldColor
                or (row, col) in visited
            ):
                return

            visited.add((row, col))
            image[row][col] = color

            helper(row + 1, col, oldColor)
            helper(row - 1, col, oldColor)
            helper(row, col + 1, oldColor)
            helper(row, col - 1, oldColor)
        
        oldColor = image[sr][sc]
        helper(sr, sc, oldColor)
        return image
            
        