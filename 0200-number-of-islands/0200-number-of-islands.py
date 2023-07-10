class Solution(object):
    def numIslands(self, grid):
        output, Rows, Cols, visited = 0, len(grid) - 1, len(grid[0]) - 1, set()
        def dfs(r,c):
            if (r < 0 or
               c < 0 or 
               r > Rows or
               c > Cols or
               grid[r][c] == "0" or
               (r,c) in visited):
                return
            visited.add((r,c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row,col)
                    output += 1
        return output
        """
        Pseudocode:
        1. Initialize variables: 
            intialize the output = 0, 
            length of the row to traverse -> Row = len(grid) - 1, 
            length of the col to traverse -> Col = len(grid[0]) - 1, 
            a hash set to keep track of the visited cells -> visited = set()
        2. DFS helps us explore a graph or a tree as deep as possible before backtracking, so we will use a helper function to traverse the cells of the matrix and explore their neighboring cells and backtrack to the cell:
            a. helper(r,c):
                i. edge cases return nothing by not calling the helper function recursively(Handle edge cases by returning if the current cell is out of bounds, already visited, or represents water.):
                    if (r < 0 or c < 0 or r >= Row or c >= Col or (r,c) in visited or grid[r][c] == "0"):
                        return 
                
                ii. if the cells haven't been visited then add it:
                        visited.add((r,c))
                ii. to explore the neighboring cells visit in four directions using helper function recursively:
                    helper(r + 1, c)
                    helper(r - 1, c)
                    helper(r, c + 1)
                    helper(r, c - 1)
        3. Using nested for loop traverse the matrix. It is used to iterate over each cell in the matrix and check if it represents land ("1").:
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    a. if the matrix value == "1" and the grid[row][col] which is the current cell is not in the visited set:
                        call the helper function (row,col)
                        increment the output by 1 as land is found
        4. Return the output that has the number of lands
        TC: O(m * n) here m is the number of rows and n is the number of columns. This is because you are traversing each cell in the matrix using nested for loops.
        SC: O(m + n) + O(n) = O(m + n) overall
            O(m + n) as we are calling the helper function on both rows and columns(recursive stack space)
            O(n) for using a hash set for visited cells
        """
        
        
        
        """
        1. Are diagonal movements considered when determining neighboring cells? - No
        2. Can we modify the input grid during the process of counting islands? - No, perform any necessary operations on a separate data structure or use additional variables to track the visited cells.
        3. Can the grid contain values other than 0 and 1? - No
        4. Are islands allowed to have disconnected components within the same island? - No, islands are typically considered as connected components of land.
        5. Is the input grid always a rectangular shape, or can it have irregular rows and columns?- Yes, it can be irregular rows and columns, it doesn't have to be perfect rectangle.
        6. Is it possible for the input grid to be extremely large, potentially causing memory issues? - Yes, it is necessary to have optimized solution
        7. Are there any constraints on the dimensions of the input grid?: We can assume that the dimensions of the grid can vary and there are no predefined limits on the number of rows or columns.
        8. How should the function handle invalid input, such as a non-list input or non-numeric values in the grid?: Always going to be 0s and 1s
        Depth-First Search (DFS) approach is a suitable technique to solve this problem. By using DFS, you can systematically traverse the cells of the matrix and explore their neighboring cells in a depth-first manner.
        """
        