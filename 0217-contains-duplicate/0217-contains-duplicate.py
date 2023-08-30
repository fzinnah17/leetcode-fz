class Solution(object):
    def containsDuplicate(self, nums):
        """
        if numbers are repeated -> return True
        if numbers are not repeated -> return False
        TC: O(1) SC: O(n)
        """
        if len(set(nums)) != len(nums):
            return True
        return False
        
        