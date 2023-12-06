class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        return indices
        sorted -> binary search
        """
        l = 0
        r = len(nums) - 1
        
        while l < r:
            curr = nums[l] + nums[r]
            
            if curr == target:
                return [l + 1, r + 1]
            elif curr > target:
                r -= 1
            else:
                l += 1
        