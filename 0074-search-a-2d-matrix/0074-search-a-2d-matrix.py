class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        
        left = 0
        right = r * c - 1
        
        while left <= right:
            middle = left + ((right - left)//2)
            middleIndex = matrix[middle // c][middle % c]
            
            if middleIndex < target:
                left = middle + 1
            elif middleIndex > target:
                right = middle - 1
            else:
                return True
        return False
    """
    TC: O(log(n * m))
    SC: O(1)"""
        