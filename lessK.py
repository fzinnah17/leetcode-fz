"""
Given an array of integers called nums and an integer k, return the largest sum for which i j such that sum = nums[i] + nums[j] and sum k. 
If there are no i and j that work with this equation, return -1.

Input:
[10,20,30]
15

Output = -1
"""

"""Optimized Approach: Two Pointers"""
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """TC: O(nlogn) SC: O(1)"""
        nums.sort()
        left = 0
        right = len(nums) - 1
        maxSum = -1
        while left < right:
            currSum = nums[left] + nums[right]
            if currSum < k:
                maxSum = max(maxSum, currSum)
                left += 1
            else:
                right -= 1
        return maxSum
      
"""
Brute Force Approach:
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        i < j
        nums[i] + nums[j] < k
        TC: O(n^2logn)
        SC: O(1)
        """
        nums.sort()
        maxSum = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                currSum = nums[i] + nums[j]
                if currSum < k:
                    maxSum = max(maxSum, currSum)
        return maxSum
"""
