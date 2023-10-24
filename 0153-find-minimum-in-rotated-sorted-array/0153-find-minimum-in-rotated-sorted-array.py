class Solution:
    """
    TC: O(logn)
    SC: O(1)"""
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right: # loop continues until it zeroes in on the inflection point.
            middle = left + ((right - left) // 2)
            if nums[middle] > nums[right]: #inflection point (minimum element) is to the right of middle, we're still in the descending part of the array.
                left = middle + 1
            else: #ascending part of the array, and the inflection point is to our left (or the middle point itself)
                right = middle 
        return nums[right]
    """
     we're comparing the middle element with the rightmost element to determine which part of the array we're in (the strictly increasing part or the part that contains the inflection point)"""