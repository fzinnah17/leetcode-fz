class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def helper(start, curr):
            result.append(curr[:])
            for i in range(start, len(nums)):
                curr.append(nums[i])
                helper(i + 1, curr)
                curr.pop()
        helper(0,[])  
        return result
        