class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        finding the middle
        if the middle > nums[right] -> move pointer to right
        else:
        mid will be right
        TC: O(logn) for dividing the search space in half with each iteration of the loop
        SC: O(1)
        """
        l, r = 0, len(nums) - 1
        
        while l < r: #looking for the point where nums[mid] becomes less than nums[r] indicating the transition from the higher values to the lower values
            mid = l + ((r-l) // 2)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r] #because mid is not defined when the loop is terminated so we use the value of right which is assigned as middle
        