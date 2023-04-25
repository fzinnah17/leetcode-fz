class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        1. Hashmap = {}
        2. iterate:
            curr = target - arr[ind]
            if curr not in hashMap:
                add the index of that curr value in the hashMap
            if it is in the hashMap:
                return [index, hashMap[curr]]
        """
        hashMap = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr not in hashMap:
                hashMap[nums[i]] = i
            else:
                return [i, hashMap[curr]]
            #TC: O(n) SC: O(n)