class Solution(object):
    def numIslands(self, grid):
        """
        Things I am considering:
        1. It is representing a 2d Matrix
        2. Boundaries/Edge cases: [r: 1,c:1], [r: 1, c: len- 1], [r: len - 1, col: 1], [r: len-1, col: len-1] to make sure I don't leave the matrix. 0 -> water -> not allowed to move
        3. Grid Constraints: not traversed diagonally
        4. Traversal of the matrix: left, right, up, or down
        5. Direction Arrays: Instead of writing different code for each traversal direction, I can save the possible movement offsets in direction arrays
        6. Visited Cells: Keep track of the cells by using a separate visited array
        7. Find and count the number of connected 1's. TASK 
        8. Figure out if all the cells [1] in the matrix are connected or how many different parts are connected. Consider using DFS or BFS to see how cells are linked.
        9. DFS because for each cell we can check each direction, and come back to the original cell to check if there are any other direction left to check
        10. Use a counter variable to keep track of how many islands are seen during traversal. Add one to the counter each time a new island is found.
        11. Look at all the choices, make a decision, and go back if you need to.
        12. Changing the traversal path if 0 is seen.
        """
        #Track visited cells
        visited = set()
        #Initialize a variable counter
        counter = 0
        #Number of rows
        Rows = len(grid) - 1
        #Number of columns
        Cols = len(grid[0]) - 1
        #Direction Arrays + Traversal of the matrix
        def helper(row, col):
            #[r: 1,c:1], [r: 1, c: len- 1], [r: len - 1, col: 1], [r: len-1, col: len-1]
            if row < 0 or col < 0 or row > Rows or col > Cols or grid[row][col] == '0' or (row,col) in visited:
                return
            visited.add((row,col)) # Mark the cell as visited
            helper(row + 1, col)
            helper(row - 1, col)
            helper(row, col + 1)
            helper(row, col - 1)
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visited:
                    helper(row, col)
                    counter += 1
        return counter
        #TC: O(m + n) SC: O(n)  