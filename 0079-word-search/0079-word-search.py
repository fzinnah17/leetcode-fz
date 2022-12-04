class Solution(object):
    def exist(self, board, word):
        #Helper function
        Rows = len(board)
        Cols = len(board[0])
        visited = set()
        def helper(row, col, index):
            if (row < 0 or row >= Rows or col < 0 or col >= Cols or 
            board[row][col] != word[index] or (row,col) in visited):
                return False
            if index == len(word) - 1:
                return True
            visited.add((row,col))
            
            found = helper(row+1,col,index+1) or helper(row-1,col,index+1) or helper(row,col+1,index+1) or helper(row,col-1,index+1)
            visited.remove((row,col)) #each path
            return found
        count = defaultdict(int, sum(map(Counter, board), Counter()))
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        for row in range(Rows):
            for col in range(Cols):
                if helper(row,col,0):
                    return True
        return False
                
            
        
            
            
            
            
            #row + 1 -> T
            #row - 1 -> T
            #col + 1 -> T
            #col - 1 -> T
            #return False
            #Not adding "D" is wise because otherwise I have to traveerse the "D" cell. 
            #"D" is the special "value: len(word)-1" of the word that returns the grid path true.
            
            
            
        
                
            
            #edge cases 
            
            #Add the values in the set
            
        