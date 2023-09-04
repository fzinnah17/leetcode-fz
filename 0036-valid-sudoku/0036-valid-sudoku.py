from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        QUICK STATE TRACKING
        1. Variables as duplicates are not allowed:
            a. A dictionary that keeps track of the numbers that have been used in each row.
            b. A dictionary that keeps track of the numbers that have been used in each col.
            c. A dictionary that keeps track of the numbers that have been used in each square.
        2. Double Loop Iteration for rows and cols
        3. Ignore Empty Cells
        4. whether the current number board[r][c] already exists in the same row, column, or 3x3 square. If it does, the Sudoku board is not valid, and the function returns False.
        5. Updating Dictionaries with the values to add
        6. If the loops finish without finding any duplicates, the board is valid, and the function returns True
        TC: O(N^2) where N is the size of the board. In a standard 9x9 Sudoku board, that is O(81), effectively O(1), a constant time operation, because we are iterating through each cell exactly once.
        SC: Worst case - O(N^2) because, each cell's value could be different, requiring a separate entry in the hashmaps. However, given that in a standard 9x9 Sudoku board each number from 1-9 can appear at most 9 times, the space required is actually quite small, effectively O(1), a constant space operation.
"""
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
            
        
        """
        using hashmaps to keep track of states for quick validation checks. Similar patterns are often used in the problems, like "Two Sum", "Valid Anagram", and "Group Anagrams".

Here's a quick summary of how this pattern applies to the code:

1. Use hashmaps or sets for quick lookups to check conditions.
2. Traverse the array (or 2D array in this case) to update the hashmaps or sets.
3. Perform validation checks during traversal to meet the problem's requirements.
Understanding how hashmaps can be used for quick state tracking and lookups is really helpful


Patterns to Recognize for Future Problems
Hashmaps for State Tracking: Hashmaps can efficiently track state (in this case, numbers that have been seen).

Spatial Hashing: square[(r//3,c//3)] is a way to map 2D coordinates into clusters (3x3 squares in this case). This technique can be useful in other contexts where you need to divide a large space into manageable 'buckets'.

Early Exit: The algorithm returns False as soon as a duplicate is found, which can be a useful strategy to reduce time complexity.

Using Sets for Uniqueness: Sets are used for constant time O(1) additions and lookups, and they don't allow duplicates, which is perfect for this problem.

Nested Loops for 2D Grids: Iterating over rows and columns in a 2D array or list is a common pattern that you've likely seen in many of your listed problems (like "Median of Two Sorted Arrays").



In the case of the Sudoku problem, the 3x3 clusters are determined by the rules of the game itself: each 3x3 square, as well as each row and each column, must contain the numbers 1 through 9 without repetition. So, the 3x3 clustering is not an arbitrary choice but one dictated by the problem constraints.
"""
        