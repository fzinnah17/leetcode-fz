class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(row, target):
            left = 0
            right = len(row) - 1
            
            while left <= right:
                middle = left + ((right - left) // 2)
                if row[middle] < target:
                    left = middle + 1
                elif row[middle] > target:
                    right = middle - 1
                else:
                    return True
            return False
        for r in range(len(matrix)):
            if helper(matrix[r], target):
                return True
        return False
        