class Solution(object):
    def maximumDifference(self, nums):
        """
        nums = [5,3,6,7,4]
        1. Two pointers: left at the start of the array, right pointer is one after
        2. Variables: maxDiff = 0
        3. Traverse the array with a sliding window technique:
                a. [5, 3]  as right = 3 < left = 5 expand the window by right += 1
                b. [5,3,6] as right = 6 > left = 5, take the minimum of the window and right - thatMin#
                   [5,3,6,7] what we can do is instead of doing right - left, we can take the first minimum (3), second minimum(5), third minimum(6) and subtract each from right
                    TO DO that we can have another pointer inside that sliding window that we can compare the values with the right pointer
        TC: O(N^2) SC: O(1)
        """
        left = 0
        right = left + 1
        maxDiff = -1
        while right < len(nums):
            runningPtr = left
            while runningPtr < right:
                if nums[right] > nums[runningPtr]:
                    maxDiff = max(maxDiff, nums[right] - nums[runningPtr])
                runningPtr += 1  
            right += 1
        return maxDiff
        