class Solution(object):
    def sortedSquares(self, nums):
        """
        Pseudocode:
        1. pointer i = 0
        2. while loop i < len(nums)
            square each value
        3. Sort that array
        TC: O(n^2logn) SC: O(1)
        """
        i = 0
        while i < len(nums):
            nums[i] = nums[i] * nums[i]
            i += 1
        return sorted(nums)
        