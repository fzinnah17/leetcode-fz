class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        if s == s[::-1]:
            return True
        return False
    #TC & SC: O(1)
        
        
        