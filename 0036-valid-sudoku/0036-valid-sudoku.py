class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Concept:
        1. Arrays and Hashing: Storing data in an array and retrieving data from the array
        2. Matrix: Implementing complex data grids or spreadsheet-like interfaces. Visualizes multi-dimensional data.
        
        For this problem, 
        a. Row data: Digits 1-9 without repetition. So, store/assign the missing data
        b. Column data: Digits 1-9 without repetition. So, store/assign the missing data
        c. Similar for the 3x3 sub-boxes
        d. Storing Data: The code uses sets (rowVisited, colVisited, squareVisited) to store data (digits) for each row, column, and 3x3 subgrid. These sets are used to keep track of digits to ensure there are no duplicates.
        e. Retrieving Data: The code retrieves data from the Sudoku board (board[r][c]) to check the validity of each cell. It checks whether a digit is already present in the corresponding sets to validate the Sudoku board.
        f. Matrix: The Sudoku board is represented as a matrix (board), and the code traverses this matrix to validate the Sudoku puzzle.
        """
        Row = len(board)
        Col = len(board[0])
        
        rowVisited = defaultdict(set)
        colVisited = defaultdict(set)
        squareVisited = defaultdict(set)

        def checkRow(r, num):
            if num in rowVisited[r]:
                return False
            return True
        
        def checkCol(c, num):
            if num in colVisited[c]:
                return False
            return True

        def checkSquare(r,c,num):
            if num in squareVisited[(r//3,c//3)]:
                return False
            return True

        for r in range(Row):
            for c in range(Col):
                if board[r][c] == ".": # Because we don't fill empty spaces in this question
                    continue
                # Edge cases
                if not (
                    checkRow(r, board[r][c]) and
                    checkCol(c, board[r][c]) and
                    checkSquare(r, c, board[r][c])
                ):
                    return False
                rowVisited[r].add(board[r][c])
                colVisited[c].add(board[r][c])
                squareVisited[(r//3,c//3)].add(board[r][c])
        return True
