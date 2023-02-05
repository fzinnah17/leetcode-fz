class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        edge cases: What happens if the array size is empty? --> IT WILL ALWAYS HAVE A SIZE
                    what happens if the array size is 1? return the len(nums)
        Brute Force: two for loops iteration
        Sorting: sort in ascending order and return the minimum #O(nlogn)
        nums= sorted(nums)
        return min(nums)
        Better Algorithm: As O(logn) time complexity is requested for, the DS I can remember is to use Binary search so that I can divide the search space into and see which direction to go?
        """
        
        """
        1. two boundaries
        2. find middle index
        3. if middle i - 1 > mid: return middle   [5,6,7,1,2,3,4]
        4. if middle > right: search on the right side as the min value is there
        5. else middle < right: search on the left side as the min value is there"""
        
        
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
                return nums[0]
        
        while left <= right:
            middle = left + ((right - left) // 2) #this is the index not value
            if nums[middle - 1] > nums[middle]:
                return nums[middle]
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
            
        
        