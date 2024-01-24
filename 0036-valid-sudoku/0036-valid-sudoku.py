class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Row = len(board)
        Col = len(board[0])
        
        visited = defaultdict(dict)

        def checkValid(r, c, num):
            if num in visited['row'].get(r, set()) or num in visited['col'].get(c, set()) or num in visited['square'].get((r // 3, c // 3), set()):
                return False
            return True

        for r in range(Row):
            for c in range(Col):
                if board[r][c] == ".":
                    continue
                if not checkValid(r, c, board[r][c]):
                    return False
                visited['row'].setdefault(r, set()).add(board[r][c])
                visited['col'].setdefault(c, set()).add(board[r][c])
                visited['square'].setdefault((r // 3, c // 3), set()).add(board[r][c])
        return True
