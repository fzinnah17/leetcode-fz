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
            middle = left + ((right - left) // 2)
            #nums = [4,5,6,7,0,1,2], target = 5
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[left]: #check if target is in the left side or to the right side
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                #if nums[middle] < nums[left]
                if nums[middle] > target or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
        return -1
                
        