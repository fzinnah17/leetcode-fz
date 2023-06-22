class Solution(object):
    def threeSum(self, nums):
        """
        """
        nums.sort()
        result = []
        for ind, num in enumerate(nums):
            if num > 0:
                break
            if ind > 0 and num == nums[ind - 1]:
                continue
            left = ind+1
            right = len(nums) - 1
            while (left < right):
                sum = num + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -=1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1 
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result
        