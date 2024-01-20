class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        nums = [4, 5, 6, 7, 0, 1, 2],  target = 5
        nums = [6, 7, 8, 1, 2, 3, 4, 5], target = 2
        choose only one side which is left and then inside that loop work with the boundaries
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            # nums = [4, 5, 6,   7,   0, 1, 2],  mid 7, target = 5
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if nums[m] > target >= nums[l]:
                #answer is in the left portion of the array
                    r = m - 1
                else:
                    l = m + 1
            #if nums[m] < nums[l]:
            else:
                if nums[m] < target <= nums[r]:
                #answer is in the right portion of the array
                    l = m + 1
                else:
                    r = m - 1
        return -1