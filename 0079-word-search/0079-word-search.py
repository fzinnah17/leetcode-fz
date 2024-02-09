class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      
      Row = len(board)
      Col = len(board[0])
      visited = set()
      
      def dfs(r, c, pointer):
        
        #base cases:
        
        if len(word) == pointer:
          return True
        
        if (r < 0 or 
            c < 0 or 
            r >= Row or 
            c >= Col or 
            (r, c) in visited or 
            board[r][c] != word[pointer]):
          return
        
        visited.add((r, c))
        res = (dfs(r + 1, c, pointer + 1) or 
               dfs(r - 1, c, pointer + 1) or 
               dfs(r, c + 1, pointer + 1) or 
               dfs(r, c - 1, pointer + 1))
        visited.remove((r,c))
        return res
      
      for row in range(Row):
        for col in range(Col):
          # if the first character matches then call the dfs function -> condition
          if board[row][col] == word[0]:
            if dfs(row, col, 0):
              return True
      return False
        