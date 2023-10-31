class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            #nums = [4,5,6,7,0,1,2], target = 0
            middle = left + ((right - left) // 2) #middle = 7
            if nums[middle] == target:
                return middle
            if nums[middle] < nums[left]: #[4,5,6,7] the answer is not in the left portion
                if nums[middle] > target or target > nums[right]: #not in left portion
                    right = middle - 1
                else:
                    left = middle + 1
            else: #if nums[middle] < nums[left]  nums = [4,5,6,7,0,1,2,3,4]
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
        