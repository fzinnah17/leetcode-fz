class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        """
        each row is in increasing order
        """
        Rows = len(matrix)
        Cols = len(matrix[0])
        
        l = 0
        r = (Rows * Cols) - 1
        
        while l <= r:
            #find medium
            m = l + ((r - l) // 2)
            #find the corresponding row and column of the medium
            midRow = m // Cols
            midCol = m % Cols
            
            if matrix[midRow][midCol] == t:
                return True
            elif matrix[midRow][midCol] > t:
                r = m - 1
            else:
                l = m + 1
        return False
                
                
        