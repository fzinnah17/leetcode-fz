class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        Pseudocode:
        1. Initialize variables: max_avg, window_avg, window_sum, start
        2. Iterate through nums:
            a. Add the current number to window_sum
            b. If the current index is greater than or equal to k - 1:
                - Calculate the window average using window_sum divided by k
                - Update max_avg with the maximum average encountered so far
                - Subtract the element at nums[start] from window_sum to remove the first element of the window
                - Increment start to slide the window
        3. Return max_avg as the maximum average
        """
        ans = float('-inf')
        currAvg = 0
        currSum = 0.0

        for i in range(len(nums)):
            currSum += nums[i]
            
            if i >= k - 1:
                currAvg = currSum / k #first find the average
                ans = max(ans, currAvg) #update the average
                currSum -= nums[i - k + 1]  #remove the first nums
                #so they did it chronologically
        return ans
    #TC: O(n) SC: O(1)
