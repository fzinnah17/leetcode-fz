class Solution:
    def shortestToChar(self, s, c):
        """
        Time: O(n^2)
        Space: O(n) + O(n) [stack space]"""
        res = [len(s)] * len(s)
        
        def helper(pos, dist):
            if res[pos] <= dist:
                return
            res[pos] = dist
            
            if pos < len(s) - 1:
                helper(pos + 1, dist + 1)
            
            if pos > 0:
                helper(pos - 1, dist + 1)
        
        for i in range(len(s)):
            if s[i] == c:
                helper(i, 0)
        return res
    