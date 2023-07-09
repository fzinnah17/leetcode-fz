class Solution(object):
    def trap(self, height):
        """
        Pseudocode:
        1. variables: 
            a. left = 0, right = len(array) - 1 as it reference both sides of the array
            b. water = 0
            c. leftMax = array[left] maximum bar heights encountered so far from the left side
            d. rightMax = array[right] maximum bar heights encountered so far from the left side
        2. Traverse the array from left to right using while loop:
            while left < right:
            The idea is to compare both leftMax and rightMax to see where the water is trapped
            a. if rightMax > leftMax:
                the water should depend on the left bar as the left bar is small
                i. left += 1
                ii. update the rightMax using the max function. max(maxLeft,array[left])
                iii. calculate the water: water += maxLeft - array[left]
            b. else: rightMax < leftMax:
                the water should depend on the right bar as the right bar is small
                i. right -= 1
                ii. update the rightMax using the max function. max(maxRight,array[right])
                iii. calculate the water: water += maxRight - array[right]
        3. Return the water variable
        TC: O(n) SC: O(1)
        """
        left, right = 0, len(height) - 1
        water, leftMax, rightMax = 0, height[left], height[right]
        
        while left < right:
            if rightMax > leftMax:
                left += 1
                leftMax = max(leftMax, height[left])
                water += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water += rightMax - height[right]
        return water
        