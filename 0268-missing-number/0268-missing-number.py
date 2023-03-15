class Solution(object):
    def missingNumber(self, nums):
        """
        TC: O(n) SC: O(1)
        psuedocode:
        1. res = len(nums) = 3
        2. traverse the array:
            res = res ^ i ^ nums[i]
                = 3 ^ 0 ^ 3 = 0
                = 0 ^ 1 ^ 0 = 1
                = 1 ^ 2 ^ 1 = 2 (return this)
        """
        res = len(nums)
        for i in range(len(nums)):
            res = res ^ i ^ nums[i]
        return res
    
        
        
        
        