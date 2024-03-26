class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, mid, r = 0, 0, len(nums) - 1

        # While the middle pointer is less than or equal to right pointer, we have not visited each number and sorted the numbers
        while mid <= r:

            # If middle pointer is pointing at a 0, then swap with the left pointer and move both left and middle pointers forward. Because we setup the left pointer spot to be ready for another zero. Middle pointer can go forward to try next number, because we are garenteed to use spot for left pointer.
            if nums[mid] == 0:
                nums[l], nums[mid] = nums[mid], nums[l]
                l += 1
                mid += 1

            # If middle pointer is pointing at a 1, then move middle pointer forward. Because, the 1 is in the right place for the middle pointer. 
            elif nums[mid] == 1:
                mid += 1
            
            # If middle pointer is pointing at a 2, then swap with the right pointer and move the right pointer backwards. Because we setup the right pointer spot to be ready for another zero. Middle pointer needs to remain at the original spot because we cannot garanteed to that spot.
            else:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
        
        return nums
        