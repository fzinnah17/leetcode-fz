class Solution:
    def trap(self, h: List[int]) -> int:
        """
        Two pointers concept is used in: 
        a. Optimizing algorithms for processing large files or streams, like handling large JSON responses in a REST API.
        b. Optimizing memory usage in file uploads or streaming services.
        c. For example, when reading and parsing a large log file, you can use two pointers to keep track of the current position and process the file in chunks, reducing memory usage and improving performance.
        d.  Instead of loading the entire file into memory, you can use two pointers to read and process the file in smaller segments, reducing the memory footprint of your application.
        
        For this problem, it is used as:
        
        Pseudocode:
        1. Keep two variables left_max and right_max to track the maximum height from the left and right sides of the current element.
        2. Use two pointers, left and right, starting from the beginning and end of the array.
        3. While the left pointer is less than or equal to the right pointer:
            a. Update left_max and right_max with the current maximum heights from left and right.
            b. If left_max is less than right_max, water can be trapped at left position, so add left_max - h[left] to res, and move the left pointer.
            c. Otherwise, water can be trapped at right position, so add right_max - h[right] to res, and move the right pointer.          
        """
        if not h:
            return 0

        left, right = 0, len(h) - 1
        leftMax, rightMax = h[left], h[right]
        res = 0

        while left < right:
            leftMax = max(leftMax, h[left])
            rightMax = max(rightMax, h[right])

            if leftMax <= rightMax:
                res += leftMax - h[left]
                left += 1
            else:
                res += rightMax - h[right]
                right -= 1

        return res
            
        