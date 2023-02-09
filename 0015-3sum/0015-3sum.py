class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)): # leave two entry for pointer
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                newSum = nums[left] + nums[right] + nums[i]
                if newSum < 0:
                    left += 1
                elif newSum > 0:
                    right -= 1
                else:
                    ans.append((nums[i],nums[left],nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    left += 1
        return ans
                    
                    
                
                
        