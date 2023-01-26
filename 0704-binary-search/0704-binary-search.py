class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Things needed in a binary tree:
        1. Sort
        2. Lower bound and upper bound
        3. Start iteration:
            a. FindMiddle element [always do integer division with //]
            b. if middle < target ,lower bound goes up to the next element of middle
            c. if middle > target, upper bound goes down to the next element of the middle
        """
        
        left, right = 0, len(nums) - 1
        
        
        while left <= right:
            middle = left + ((right - left) // 2)
            if nums[middle] == target:
                return middle #index
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1
    #TC: O(nlogn) SC: O(1)
        
            
        