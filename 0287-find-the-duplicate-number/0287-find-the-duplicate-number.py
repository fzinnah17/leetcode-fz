class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #TC+ SC: O(n)
        hashSet = set()
        
        for i in nums:
            if i in hashSet:
                return i
            hashSet.add(i)
            
        
        