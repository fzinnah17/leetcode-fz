class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        countParent = 0
        maxNumparent = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                countParent += 1
                maxNumparent = max(maxNumparent, countParent)
            
            if s[i] == ')':
                countParent -= 1
        return maxNumparent
        