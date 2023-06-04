class Solution(object):
    def maxSubArray(self, nums):
        """
        1. Handle edge cases/constraints
        2. Initialize variables: sum
        3. Calculate the initial result: Of the first window and check if it is > 0 or < 0
        4. Slide the window: Iterate through the array or linked list using a loop, adjusting the sliding window by moving the start and end indices as needed
        5. Update the result: The result will be updated based on the current window.
                I. Determine the sliding window size: We can start by making the window size expand one at a time.
                    a. if the addition of the window size is < 0, then we can remove the first number of the window
                    b. if the addition of the window size is > 0 or > prevSum, then keep expanding the window
        6. we will return the sum using max() function
        """
        ans = float("-inf")
        runSum = 0
        for i in range(len(nums)):
            if runSum < 0:
                runSum = nums[i]
            else:
                runSum += nums[i]
            ans = max(ans, runSum)
        return ans
    #TC: O(n) SC: O(1)
            
    """Lesson:
the equal sign (=) is used for assignment, while the double equal sign (==) is used for comparison.

When you write runSum = nums[i], you are assigning the value of nums[i] to the variable runSum. This means that runSum will now hold the same value as nums[i].

On the other hand, when you write runSum == nums[i], you are checking if the value of runSum is equal to the value of nums[i]. This expression will return either True or False, depending on whether the values are equal or not.
"""
        
        
        