class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        Pseudocode:
            1. Go through each cell in the matrix one at a time.
                A. If the cell value and source color (sr, sc) are the same, then:
                - Change the color of the cell by changing its value.
                - Try out the four directions (up, down, left, and right):
                - Do the steps again if the value of the neighboring cell is the same as the value of the source cell.
                - Don't go in that direction if the cell next to it has a different value or is outside the parameters.
            2. Get the modified matrix back.


            I. Go through each cell in the matrix iteratively:
            - This is accomplished through the use of two nested loops that traverse the matrix's rows and columns.

            II. If the cell value and the source color (sr, sc) are the same:
            - We determine whether the current cell's value matches the source color. If it does, we will begin the flood-fill operation.
            - If the cell value is different, we skip it and proceed to the next cell.

            III. Update the value of the current cell to the new color: - Because it is part of the connected region that needs to be filled, we update the value of the current cell to the new color.

            IV. Look into the four directions (up, down, left, and right):
            - We check the neighboring cells in all four directions (up, down, left, and right) from the current cell recursively.
            - If a neighboring cell has the same value as the source color, we repeat the process on that cell to continue the flood fill operation.
            - We stop exploring that direction if a neighboring cell has a different value or is out of bounds.

            V. Return the modified matrix: We return the modified matrix after performing the flood fill operation.

            TC: Because the algorithm potentially visits each cell in the matrix once, the time complexity is O(m * n), where m and n are the matrix dimensions.
            SC: The visited set can store up to O(m * n) cell coordinates in the worst-case scenario, where all cells have the same value as the source color. Furthermore, the recursion stack can go as deep as the number of cells in the connected region.
                However, if the space used by the input matrix is ignored, the extra space required by the algorithm (visited set and recursion stack) is O(m + n) because we only store the visited cell coordinates.


        """
        Rows = len(image) - 1
        Cols = len(image[0]) - 1
        visited = set()
        sourceColor = image[sr][sc]
        def helper(row, col, sourceColor):
            if (
            row < 0
            or col < 0
            or row > Rows
            or col > Cols
            or (row,col) in visited
            or image[row][col] != sourceColor):
                return
            visited.add((row,col))
            image[row][col] = color
            helper(row + 1,col,sourceColor)
            helper(row - 1,col,sourceColor)
            helper(row,col + 1,sourceColor)
            helper(row,col - 1,sourceColor)
        helper(sr,sc,sourceColor)
        return image
        
            
        