class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set) #()
        colSet = defaultdict(set) #()
        squareSet = defaultdict(set) #()
        
        #functions are for debugging processes -> easily identify what's wrong
        #check from the board:
        """
        breaking the logic down
            a. function(params):
                    same logic but specific r,c,s
                        False
                    True
        not function(params) -> False
        """
        #check row
        def checkRow(r,num):
            if num in rowSet[r]:
                return False
            return True

        #check col
        def checkCol(c,num):
            if num in colSet[c]:
                return False
            return True
        
        #check box
        def checkSquare(r,c,num):
            if num in squareSet[(r//3,c//3)]:
                return False
            return True
            
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if not(checkRow(r,board[r][c]) and checkCol(c,board[r][c]) and checkSquare(r,c,board[r][c])):
                    return False
                rowSet[r].add(board[r][c])
                colSet[c].add(board[r][c])
                squareSet[(r//3,c//3)].add(board[r][c])
        return True
        