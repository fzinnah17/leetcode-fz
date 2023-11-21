class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        left, right = 0, 0
        
        visited = set()
        # "abcabcbb"
      # set = b, c, a, 
        
        while right < len(s):
            #sliding window
            if s[right] not in visited:
                visited.add(s[right])
                output = max(output, right - left + 1)
            #right pointer moves
                right += 1
            else:
                visited.remove(s[left])
                left += 1
        return output
                
            
        
        