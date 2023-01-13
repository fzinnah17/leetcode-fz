class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        1. start
        2. end pointer = len(nnums) - 1:
        3. whichever square is bigger add it into the result array
        
        """
        # return [i**2 for i in nums]
        
        start = 0
        end = len(nums) - 1
        result = []
        while (start <= end):
            if nums[start]**2 <= nums[end]**2:
                result.append(nums[end]**2)
                end -= 1
            else:
                result.append(nums[start]**2)
                start += 1
        return result[::-1]
    #O(n) for both time and space complexity
                
        