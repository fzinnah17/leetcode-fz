class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        1. array is sorted increasingly/order cant be changed
        2. remove the duplicates in place
        3. each element appears only once  <- return it
        4. 
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
                       i
                       j
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Pseudocode:
        1. two pointers
        2. while loop
            if i and j values match:
                j += 1
                swap j value with it's previous val
  
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i+1)
            else:
                i += 1
        return i+1
            
        