class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Pseudo-code:
        1. create two pointers (one to increment and another for the zero value)
        2. As we are traversing the length of the list,
            a. if the number is non-zero, then swap it with zero value
            b. increment the zero pointer till it reaches the boundary
        3. increment the iTH pointer for the while loop to interate the length of the list completely
        4. We don't return anything as we are not required to return anything
        TC: O(n)
        SC: O(n)
        """
        i = 0
        numZero = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[numZero] = nums[numZero], nums[i]
                numZero += 1
            i += 1
                
            
        
        