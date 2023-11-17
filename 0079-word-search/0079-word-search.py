class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        Rows = len(board)
        Cols = len(board[0])
        
# [["C","A","A"]
#  ["A","A","A"]
#  ["B","C","D"]]
# "AAB" 
        
        visited = set()
        def dfs(r,c, pointer):
            if len(word) == pointer:
                return True
            
            if ( r < 0 or
               c < 0 or 
               r >= Rows or
               c >= Cols or
                board[r][c] != word[pointer] or
                (r,c) in visited
               ):
                return
            
            visited.add((r,c))
            
            result = (
            dfs( r + 1, c, pointer + 1) or 
            dfs( r - 1, c, pointer + 1) or
            dfs( r, c + 1, pointer + 1) or
            dfs( r, c - 1, pointer + 1))
            
            visited.remove((r,c))

            return result
        
        for row in range(Rows):
            for col in range(Cols):
                
                if board[row][col] == word[0]:
                    if dfs(row,col, 0):   
                        return True
        return False
        