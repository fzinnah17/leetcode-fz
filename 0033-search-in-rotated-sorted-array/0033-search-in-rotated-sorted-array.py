class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        TC: O(logn) for dividing the search space in half with each iteration of the loop
        SC: O(1)
        It all depends on mid value so 
            if left val < mid
                left half?
                right half?
            if left val > mid
                right half?
                left half?
        
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)

            # Check if the middle element is the target
            # nums = [1, 2, 3, 4, 5]
            # target = 3
            # Middle value m = 2
            if nums[m] == target:
                return m

            # If the left side is sorted from min val
            # nums = [4, 5, 6, 7, 0, 1, 2]
            # target = 5
            # Middle value index m = 3, value = 7
            if nums[l] <= nums[m]:
                # Check if the target is in the left half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                # if target = 1
                else:
                    l = m + 1
            # If the right side is sorted from min val
            #if nums[l] > nums[m]
            #Example: nums = [6, 7, 8, 1, 2, 3, 4, 5], target = 2, middle index = 3(value = 1)
            else:
                # Check if the target is in the right half target = 3
                if nums[m] < target <= nums[r]:
                    l = m + 1
                #target = 8
                else:
                    r = m - 1
        return -1