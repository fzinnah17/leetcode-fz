class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        Optmized: TC: O(n) SC: O(n)
        """
        count = 0
        hashSet = set(nums)
        #(1,4,7) diff = 3  4 - 3 = 1 and 4 + 3 = 7 both in the set
        #(4,7,10) diff = 3 7 - 3 = 4 and 7 + 3 = 10 both in the set
        for i in range(len(nums)):
            subNum = nums[i] - diff
            addNum = nums[i] + diff
            if subNum in hashSet and addNum in hashSet:
                count += 1
        return count
            
            
"""Brute Force: O(n^3)
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        count += 1
        return count"""
        