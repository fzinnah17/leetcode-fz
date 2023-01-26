class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        non-decreasing = increasing
        things needed for Binary search:
        1. bounds: upper and lower [For Matrix, the last pointer is the final value third row bottom right last element, FORMULA: rows*cols-1]
        2. iteration
            a. middle element: left + ((right - left)//2) to avoid overflow
                check if middle == target: return true
                middle > target -> upper bound = middle - 1
                middle < target -> lower bound = middle + 1
                
        3. For any 2D, 
            a. To print each element of Matrix/ 2D matrix iteration format:
                for i in range(len(data)):
                    for j in range(len(data[i])):
                        print(data[i][j], " ")
            b. Rows = len(grid) [[[- 1]]], Cols = len(grid[0]) [[[[- 1]]]] -1 MIGHT OR MIGHT NOT NEEDED
            c. currRow = middle // cols
               currCol = middle % cols  {{{{THESE ARE THE FORMULAS TO FIND CURRENT POSITION}}}}
        """
        rows = len(matrix)
        cols = len(matrix[0]) 
        
        left = 0 #0th index has left pointer
        right = rows * cols - 1 #final value third row bottom right last element has right pointer
        
        while left <= right:
            middle = left + ((right - left)//2)
            currRow = middle // cols
            currCol = middle % cols
            if matrix[currRow][currCol] == target:
                return True
            if matrix[currRow][currCol] > target:
                right = middle - 1
            elif matrix[currRow][currCol] < target:
                left = middle + 1
        return False
        