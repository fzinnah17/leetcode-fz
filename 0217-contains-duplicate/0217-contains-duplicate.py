class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t = set(nums)
        if len(nums) != len(t):
            return True
        return False
        