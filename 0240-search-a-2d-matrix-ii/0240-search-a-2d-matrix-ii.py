class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(r, target):
            left = 0
            right = len(r) - 1
            
            while left <= right:
                middle = left + ((right - left) // 2)
                if r[middle] < target:
                    left = middle + 1
                elif r[middle] > target:
                    right = middle - 1
                else:
                    return True
            return False
             
        for row in matrix:
            if helper(row, target):
                return True
        return False
    """
    TC: binary search is O(logn), and since we perform binary search on all the rows, the final time complexity of the whole solution is O(nlogn).
    SC: O(1)
"""
            
        