class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      """
      while loop
      iterate and keep on adding the right pointer values
      if right val > 1: we decrease the left count from the window
      if left count == 0: we remove it from the window
      as we are doing this algorithm, we are 
      """
      
      l, r = 0,0
      visited = set()
      length = 0
      
      while r < len(s):
        if s[r] in visited:
          visited.remove(s[l])
          l += 1
        else:
          visited.add(s[r])
          length = max(length, r - l + 1)   
          r += 1
        
      return length
          
        
        