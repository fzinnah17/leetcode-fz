class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        """
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                        count += 1
        return count
        