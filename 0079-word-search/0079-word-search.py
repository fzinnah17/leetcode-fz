class Solution(object):
    def exist(self, board, word):
        """
        Pseudocode:
        1. variables: numRows = len(grid), numCols = len(grid[0]), visited = set()
        2. Helper function(r,c, pointer):
            a. if pointer == len(word):
                return True This line is used to determine whether or not the target word was found in the given grid. We have successfully matched all of the word's characters with the characters in the grid and found the target word when the pointer reaches the length of the word. In this case, we can return True to indicate that the word exists in the grid.

Without this check, recursive calls would continue even after the target word was found, which might result in more calculations and incorrect results. We can end the recursive calls as soon as the word is found by checking if the pointer has reached the length of the word, improving the algorithm's efficiency.

            b. boundaries: if(r < 0 or c < 0 or r >= numRows or c >= numCols or grid[r][c] != word[pointer] or (r,c) in visited):
                return
            c. Add to the hashset: visited.add((r,c))
            d. call the helper functions in four directions and it in a result variable:
                result = (
                (r + 1, c, pointer + 1) or (r - 1, c, pointer + 1) or (r, c + 1, pointer + 1) or (r, c - 1, pointer + 1)
                ) We use the result variable because if any of the recursive calls returns True, we have found the target word and can use the recursive calls to return the result to the original caller. If none of the recursive calls returns True, we'll keep looking in different directions until we either find the word or have exhausted all possibilities.
            d. visited.remove((r,c)): Remove the cell from the visited set after exploring all four directions. This is crucial because once you've tried all four directions and haven't found the word, you need to backtrack, removing the current cell from visited so it can be used in a different potential word path.
        3. Traverse the board in rows: numRows
                Traverse the board in columns: numCols
                    if helper(row,col,0):
                        return True when you've found a match for the entire word.
            return False outside of the for loop in order to show that the word was never found
        TC: O(m * n) SC: O(m * n)
        """
        numRows = len(board)
        numCols = len(board[0])
        visited = set()
        def helper(r, c, pointer):
            if pointer == len(word):
                return True
            if (r < 0 or c < 0 or r >= numRows or c >= numCols or board[r][c] != word[pointer] or (r,c) in visited):
                return
            visited.add((r,c))
            res = (
                helper(r + 1, c, pointer + 1) or
            helper(r - 1, c, pointer + 1) or
            helper(r, c + 1, pointer + 1) or
            helper(r, c - 1, pointer + 1)
            )
            visited.remove((r,c))
            return res
        for row in range(numRows):
            for col in range(numCols):
                if helper(row, col, 0):
                    return True
        return False
        