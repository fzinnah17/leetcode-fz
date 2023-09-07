class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. Initialize the result array
        2. Variables: Initialize the prefix and postfix
        3. Multiply by prefix product
        4. Multiply by postfix product
        5. update the prefix product
        6. update the postfix product
        7. return the result array"""
        n = len(nums)
        res = [1] * n
        
        preFix = 1
        postFix = 1
        
        for i in range(n):
            res[i] *= preFix
            res[n-1-i] *= postFix
            
            preFix *= nums[i]
            postFix *= nums[n - 1 - i]
        return res