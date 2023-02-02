class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Infix	  Prefix	Postfix/Suffix
         A+B	   +AB	      AB+
        """
        preFix, postFix = [1]*len(nums), [1]*len(nums)
        
        for i in range(1,len(nums)):
            preFix[i] =  preFix[i-1]*nums[i-1]
        for i in reversed(range(0, len(nums)-1)):
            postFix[i] = postFix[i+1]*nums[i+1]   
        for i in range(len(nums)):
            nums[i] = preFix[i]*postFix[i]
        return nums
        
        
        