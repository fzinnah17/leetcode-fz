"""Problem Statement
Given an array of positive numbers and a positive number 'k,' find the maximum sum of any contiguous subarray of size 'k'.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4]."""
  
  
  
def maxSumofK(nums, k):
  ans = float("-inf")
  runSum = 0
  for i in range(len(nums)):
    if i >= k:
      runSum -= nums[i-k]
    if runSum < 0:
      runSum = nums[i]
    else:
      runSum += nums[i]
    if i >= k - 1:
      ans = max(ans,runSum)
  return ans


"""TC: O(n) for number of elements in the array. SC: O(1) for no space used"""
     
  
