class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Infix	  Prefix	Postfix/Suffix
         A+B	   +AB	      AB+
        """
        #TC: O(n) and SC: O(1)
        res= [1]*len(nums)
        preFix = 1
        postFix = 1
        
        for i in range(len(nums)):
            res[i] *= preFix
            res[(len(nums)-1)-i] *= postFix
            #preFix and postFix are updated on each block
            preFix *= nums[i]
            postFix *= nums[(len(nums)-1)-i]            
        return res
        """
        For our initial array, we want to find the Prefix Product Array and PostFix Product Array. preFix[i] = preFix[i - 1] * nums[i - 1], for example. (Yes, we multiply with nums[i - 1] rather than nums[i]), and postFix[i] = postFix[i + 1] * nums[i + 1].
Now, for each index i, our final answer would be result[i] = preFix[i] * postFix[i]. Why? Because preFix[i] * postFix[i] contains the product of each element before and after i, but not the one at index i. (As a result, nums[i] was not included in our preFix and postFix products.)

The Time Complexity would be O(n), but we already have O(n) Auxiliary Space (excluding the final answer array).
        preFix, postFix = [1]*len(nums), [1]*len(nums)
        
        for i in range(1,len(nums)):
            preFix[i] =  preFix[i-1]*nums[i-1]
        for i in reversed(range(0, len(nums)-1)):
            postFix[i] = postFix[i+1]*nums[i+1]   
        for i in range(len(nums)):
            nums[i] = preFix[i]*postFix[i]
        return nums"""
        
        
        