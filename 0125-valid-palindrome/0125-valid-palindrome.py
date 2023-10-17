class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def helper(c):
            return c.isalpha() or c.isdigit()
        left = 0
        right = len(s) - 1
        
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