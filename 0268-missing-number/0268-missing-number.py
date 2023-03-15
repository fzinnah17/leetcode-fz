class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #ITERATE THRU THE ARRAY
        #maybe have a dictionary from 0 to 9, but it is impossible because 10^4
        # O(1) : Space, O(n): Runtime
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res
    
        
        
        
        