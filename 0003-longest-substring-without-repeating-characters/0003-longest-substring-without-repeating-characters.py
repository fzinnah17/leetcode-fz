class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        output = 0
        visited = set()
        
        
        while r < len(s):
            if s[r] not in visited:
                visited.add(s[r])
                output = max(output, r - l + 1)
                r += 1
            else:
                visited.remove(s[l])
                l += 1

        return output
                
        