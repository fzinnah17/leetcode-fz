class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """
      left and right pointers check. if the characters are the same remove the first character from the window"""
      res = 0
      l, r = 0, 0
      visited = set()
      
      while r < len(s):
        if s[r] not in visited:
          visited.add(s[r])
          res = max(res, r - l + 1)
          r += 1
        else:
          visited.remove(s[l])
          l += 1
      return res
        
        