class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        start = 0
        end = len(nums)-1
        while nums < len(nums):
        1. sum > target:
            end -= 1
        2. sum < target:
            start += 1
        3. sum == target:
            return []   
            nums = [2,7,11,15]
        """
        start = 0
        end = len(nums) - 1
        while (start <= end):
            curr = nums[start] + nums[end]
            if curr == target:
                return [start, end]
            end -= 1
            if start == end:
                start += 1
                end = len(nums) - 1

        
        