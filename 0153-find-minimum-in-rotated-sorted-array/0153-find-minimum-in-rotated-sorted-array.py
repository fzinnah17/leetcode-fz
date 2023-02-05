class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Brute Force: two for loops iteration
        Sorting: sort in ascending order and return the minimum
        """
        nums= sorted(nums)
        return min(nums)
        
        
        