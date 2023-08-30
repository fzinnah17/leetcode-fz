class Solution(object):
    def isAnagram(self, s, t):
        """
        TC: O(n) SC: O(n)
        """
        if Counter(s) == Counter(t):
            return True
        return False