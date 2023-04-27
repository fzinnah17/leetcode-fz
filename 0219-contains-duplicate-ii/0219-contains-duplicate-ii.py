class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                if abs(i - hashMap[nums[i]]) <= k:
                    return True
                else:
                    hashMap[nums[i]] = i
        return False
                