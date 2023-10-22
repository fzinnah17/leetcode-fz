class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1
        while left <= right:
            middle = left + ((right - left) // 2)
            middleIndex = matrix[middle // col][middle % col]
            if middleIndex < target:
                left = middle + 1
            elif middleIndex > target:
                right = middle - 1
            else:
                return True
        return False
        