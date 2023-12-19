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
        
        rowVisited = []
        for _ in range(Row):
            rowVisited.append(set())

        colVisited = []
        for _ in range(Col):
            colVisited.append(set())

        squareVisited = []
        for _ in range(9):
            squareVisited.append(set())

        
        def checkRow(row, num):
            if num in rowVisited[row]:
                return False
            return True
        
        def checkCol(col, num):
            if num in colVisited[col]:
                return False
            return True

        def checkSquare(row, col, num):
            square = (row // 3) * 3 + col // 3
            if num in squareVisited[square]:
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
                square = (r // 3) * 3 + c // 3
                squareVisited[square].add(board[r][c])
        return True
