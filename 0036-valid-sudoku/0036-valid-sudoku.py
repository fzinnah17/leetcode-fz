class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROW, COL = len(board), len(board[0])
        row, col, grid = defaultdict(list), defaultdict(list), defaultdict(list)
        
        # row = {index:[values]}
        # col = ()
        # grid = ()
                
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                
                if board[r][c] == ".": continue

                # check if seen
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in grid[(r // 3, c // 3)]:
                    return False
                
                # add new char
                row[r].append(board[r][c])
                col[c].append(board[r][c])
                grid[(r // 3, c // 3)].append(board[r][c])
                
        return True
            
            
        
        