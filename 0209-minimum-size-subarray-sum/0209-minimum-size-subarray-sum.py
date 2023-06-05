class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        Edge case: If there is no such subarray, return 0 
        Initialize variables: runningSum, length
        Determine the sliding window size: It will expand as we add the numbers to reach target
            if sum > target subtract the value of the first index in the window
            length -= 1
            if sum < target, then expand the window
            length += 1
            if sum == target:
            using min function for length (4, "inf") -> return 4 #target = 7, nums = [2,3,1,1,4,3]
            [2,3,1,1] = 7

            using min function again for length (2,4) -> return 2 #target = 7, nums = [4,3]
            [4,3]         
        """
#         window_sum = 0
#         min_length = float("inf")
#         window_start = 0

#         for window_end in range(0, len(nums)):
#             window_sum += nums[window_end]  # add the next element
#         # shrink the window as small as possible until the 'window_sum' is smaller than 's'
#             while window_sum >= target:
#                 min_length = min(min_length, window_end - window_start + 1)
#                 window_sum -= nums[window_start]
#                 window_start += 1
#         if min_length == float("inf"):
#             return 0
#         return min_length
        currSum = 0
        length = float("inf")
        s = 0

        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target:
                length = min(length, i - s + 1)
                currSum -= nums[s]
                s += 1
        if length == float("inf"):
            return 0
        return length
    
    #TC: O(n) SC: O(1) 
                