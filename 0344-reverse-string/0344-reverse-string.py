class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        return s.reverse() #time: O(n) space: o(1)
        """
        l = 0
        r = len(s) - 1
        
        #we don't know how many times we will iterate
        
        while l < r:
          s[l], s[r] = s[r], s[l] 
          l += 1
          r -= 1
        print(s)
          