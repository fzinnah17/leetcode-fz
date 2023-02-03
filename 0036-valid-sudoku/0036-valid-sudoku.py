from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        To solve this problem, we must determine whether each sudoku value does not repeat in its: COLUMN/ ROW/ SQUARE
    To do this efficiently, we will use sets to store elements in columns, rows, and squares. Columns and rows are easy to define (by a single index), but squares require two indices. To determine which square we are currently in, we will use the // (floor division) operator.
    We obtained three separate values for each range (0-2: 0, 3-5: 1, 6-8: 2), which can be used to determine which square we are now in (by getting square x and y coordinates, we require nine squares with indices (0, 0), (0, 1), (0, 2), (1,0),..., (2, 2)).

If we find the "." sign in code, we do nothing; but, if we encounter a digit in a cell, we determine if it is in the row, column, or square.
If the value is repeated, the sudoku is invalid and False is returned.

After checking, we add this value to the relevant row, column, and square.
If a number occurs twice in a row, column, or square, the second occurrence yields a False result (because in first occurrence we add the value to the sets).
        """
        
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]:
                        return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
                
                        
        