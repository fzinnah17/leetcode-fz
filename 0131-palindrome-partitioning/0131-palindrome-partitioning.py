class Solution:
    def partition(self, s: str) -> List[List[str]]:
      
      """
      Time: O(2^n)"""
      
      res = []
      partitions = []
      
      if len(s) == 1:
        return [[s]]
      
      def palindrome(s):
        l, r = 0, len(s) - 1
        
        while l < r:
          if s[l] != s[r]:
            return False
          l += 1
          r -= 1
        return True
      
      def dfs(i):
        
        #base case
        if i >= len(s):
          res.append(partitions[:])
          return
        
        for j in range(i, len(s)):
          if palindrome(s[i: j + 1]):
            partitions.append(s[i:j+1])
            dfs(j + 1)
            partitions.pop()
        
      dfs(0)
      
      return res
        