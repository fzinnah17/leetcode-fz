class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashMap = {}
        
        for i in nums:
            if i in hashMap:
                hashMap[i] += 1
                if hashMap[i] > 1:
                    return True
            else:
                hashMap[i] = 1