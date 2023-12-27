class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)  # Sorting the array is not necessary for a binary search.
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:  # Change the condition to include equality.
            mid = l + ((r - l) // 2)
            
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:  # Adjust the comparisons here.
                r = mid - 1
            else:
                l = mid + 1
        return -1
