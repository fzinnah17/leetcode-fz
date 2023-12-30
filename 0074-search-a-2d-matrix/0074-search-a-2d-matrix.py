class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        variables: row, column
        """
        Row = len(matrix)
        Col = len(matrix[0])
        # print(matrix[0][0]) 1
        # print(matrix[Row - 1][Col - 1]) 60
        # print(Row * Col - 1) <- this is for length
        top, bottom = 0, Row * Col - 1
        # print(top, bottom)
        # mid = (top + ((bottom - top) // 2))
        while top <= bottom:
            mid = (top + ((bottom - top) // 2))
            mid_value = matrix[mid // Col][mid % Col]
            if mid_value == target:
                return True
            elif mid_value > target:
                bottom = mid - 1
            else:
                top = mid + 1
        return False
            