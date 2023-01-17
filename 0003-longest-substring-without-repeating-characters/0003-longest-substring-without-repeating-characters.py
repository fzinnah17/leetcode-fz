class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        left = 0, right = 1
        right < len(s):
        if right != left:
        expand the window len += 1
        if right == left:
        shrink the window 
        """
        maxLen = 0
        left, right = 0,0
        hashSet = set()
        while right < len(s):
            while s[right] in hashSet:
                hashSet.remove(s[left])
                left += 1
            hashSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            right += 1
        return maxLen
            
        
        