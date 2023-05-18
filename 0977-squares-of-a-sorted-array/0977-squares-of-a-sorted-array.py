class Solution(object):
    def sortedSquares(self, nums):
        """
        Pseudocode:
        1. two pointers = left, right
        2. empty array = []
        3. while loop till the values cross each other
            a. compare the absolute value of both pointers
                    i. greater value means larger square
                    Check condition: whichever has the largest square append it to the list
            b. Move left or right depending on the value that has been used
        4. Repeat the process
        5. Return the new array
        In our earlier approach, we did not use any space, but here we are, so there is a tradeoff with space, hence the 
        Space complexity is O(1).
        TC: O(n)"""
        left, right = 0, len(nums) - 1
        new_arr = []
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                left_num = nums[left] * nums[left]
                new_arr.append(left_num) #append the element to the end of the list.
                left += 1
            else:
                right_num = nums[right] * nums[right]
                new_arr.append(right_num)
                right -= 1
        return new_arr[::-1] #[::-1] means reversing
                
                
        
        # """
        # Pseudocode:
        # 1. pointer i = 0
        # 2. while loop i < len(nums)
        #     square each value
        # 3. Sort that array
        # TC: O(n^2logn) SC: O(1)
        # """
        # i = 0
        # while i < len(nums):
        #     nums[i] = nums[i] * nums[i]
        #     i += 1
        # return sorted(nums)
        