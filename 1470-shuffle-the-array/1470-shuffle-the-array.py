class Solution(object):
    def shuffle(self, nums, n):
        """
        Pseudocode:
        1. Find the middle value of the array
        2. Traverse the array till the middle point it is because we are swapping elements from the first and second halves of the list. After that, the list will be in the appropriate order, and there is no need to continue traversing.
        3. take the next value of middle to swap
        4. delete that value
        5. add that value to it's corresponding position
        TC: O(n) Traversing only the first half of the list is also more efficient than traversing the entire list, especially for large inputs, since it reduces the number of iterations required.
        SC: O(1)
        """
        middle = len(nums) // 2
        for i in range(middle):
            right = nums[middle + i]
            del nums[middle + i]
            nums.insert(i*2+1,right)
        return nums
            
        
        