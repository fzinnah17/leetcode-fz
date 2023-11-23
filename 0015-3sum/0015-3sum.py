class Solution(object):
    def threeSum(self, nums):
        """
        [-4, -1, -1, 0, 1, 2]
        [[-1,-1,2],[-1,0,1]]
        """
        nums.sort()
        res = [] #beacuse returning list inside of a list
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                curr = nums[left] + nums[right] + nums[i]
                if curr > 0:
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        # if nums[left] == nums[left + 1]:
                            left += 1
        return res
                
                
        