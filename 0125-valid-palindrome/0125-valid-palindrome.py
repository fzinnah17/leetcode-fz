class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointers concept is used in: 
        a. Optimizing algorithms for processing large files or streams, like handling large JSON responses in a REST API.
        b. Optimizing memory usage in file uploads or streaming services.
        c. For example, when reading and parsing a large log file, you can use two pointers to keep track of the current position and process the file in chunks, reducing memory usage and improving performance.
        d.  Instead of loading the entire file into memory, you can use two pointers to read and process the file in smaller segments, reducing the memory footprint of your application.
        
        For this problem, it is used as: efficient character comparison within a string.  It is keeping track of the current position on both sides and processing it in chunks, reducing the memory usage and improving performance.
        
        Pseducode:
        1. left begin, right end
        2. check if each letters are same, 
            if so, increment both pointers
            if any of those is " "space, then increment that pointer/skip that position
            return true if all the characters match
        3. if not found, false
        """
        s = s.lower()
        
        left, right = 0, len(s) - 1
        
        def helper(ch):
            return ch.isalpha() or ch.isdigit()
        
        while left < right:
            while left < right and not helper(s[left]):
                left += 1
                
            while left < right and not helper(s[right]):
                right -= 1
            
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1
        
        return True
        