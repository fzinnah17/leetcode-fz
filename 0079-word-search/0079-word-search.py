class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        
        def dfs(r,c,pointer):
            if len(word) == pointer:
                return True
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visited or board[r][c] != word[pointer]:
                return False
            
            visited.add((r,c))
            
            res = (
                dfs(r + 1, c, pointer + 1) or
                dfs(r - 1, c, pointer + 1) or
                dfs(r, c + 1, pointer + 1) or
                dfs(r, c - 1, pointer + 1)
            )
            
            visited.remove((r,c))
            return res
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if dfs(row,col,0):
                        return True
        return False