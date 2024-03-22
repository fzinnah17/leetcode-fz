class Solution:
    
    #closure approach -> inner function has access to all the global variables
    
    def validPalindrome(self, s: str) -> bool:
        #this is a nested function that requires not passing the string
        def is_palindrome(skips, left, right):
            if skips > 1:
                return False

            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    skips += 1
                    left_skip = is_palindrome(skips, left + 1, right)
                    right_skip = is_palindrome(skips, left, right - 1)
                    return left_skip or right_skip
            return True
        
        return is_palindrome(0, 0, len(s) - 1)
    
        
"""        test driven way to write as minimum code as possible to make the test cases 'a', 'aa', 'aaa', 'aba', 'abba' work
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
        return True"""
        