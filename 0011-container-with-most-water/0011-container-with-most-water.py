class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            if height[left] > height[right]:
                min_height = height[right]
                min_pointer = right
            else:
                min_height = height[left]
                min_pointer = left
            max_area = (right - left) * min_height
            area = max(area, max_area)
            if left == min_pointer:
                left += 1
            if right == min_pointer:
                right -=1
    
        return area 
        