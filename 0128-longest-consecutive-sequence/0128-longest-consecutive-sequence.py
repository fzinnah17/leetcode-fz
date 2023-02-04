class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums) #set([0, 1, 2, 3, 4, 5, 6, 7, 8, 14, 17, 25])
        
        longest = 0
        res = 0
        for n in nums:
            if n - 1 not in s:
                longest = 1
                while n + 1 in s:
                    longest += 1
                    n += 1
                res = max(res, longest)
        return res
                
            
            