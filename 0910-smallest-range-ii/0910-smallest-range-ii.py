class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = nums[-1] - nums[0]  # Initial range
        
        for i in range(len(nums) - 1):
            # Current number is nums[i]
            a = nums[i]
            b = nums[i + 1]
            
            # Scenario 1: Increase all previous elements by k
            max_val_1 = max(nums[-1] - k, a + k)
            min_val_1 = min(nums[0] + k, b - k)
            range_1 = max_val_1 - min_val_1
            
            # Scenario 2: Decrease all previous elements by k
            max_val_2 = max(a - k, nums[-1] + k)
            min_val_2 = min(nums[0] - k, b + k)
            range_2 = max_val_2 - min_val_2

            # Choose the smallest range
            res = min(res, range_1, range_2)

        return res
