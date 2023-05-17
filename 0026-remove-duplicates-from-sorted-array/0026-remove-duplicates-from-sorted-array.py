class Solution(object):
    def removeDuplicates(self, nums):
        """
        Things to notice:
        1. The nums array is sorted
        
        Things asked me to do:
        1. Remove the duplicates in space -> SC: O(1) can't use additional memory
        2. The order of the array should be the same
        3. Return the length of the new array
        
        Pseudocode:
        1. a pointer i = 0
        2. while loop to traverse the array
        3. check conditions:
            if i and [ i+ 1 ] is same, then remove i + 1 using the pop method as it is already a list aka stack
            if it is not the same, then increment i by i += 1 knowing it is sorted
        4. return i + 1 because i is in the last unique element
        #TC: O(n) SC: O(1)
        """
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i+1)
            else:
                i += 1
        return i+1 #it is because at the end of the iteration, i is in the last unique element
        