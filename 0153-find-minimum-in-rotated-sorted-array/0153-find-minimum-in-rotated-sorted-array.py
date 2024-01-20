class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        nums = [4,5,6,7,0,1,2]
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            
            #if middle > nums right nums = [4,5,6, 7 ,0,1,2] answer is in the right side of the array
            if nums[m] > nums[r]:
                l = m + 1
            #if middle < nums right nums = [6, 7, 8,   1,   2, 3, 4, 5] so answer is on the other side
            elif nums[m] < nums[r]:
                r = m 
            else:
                return nums[m]
                
            
        
        