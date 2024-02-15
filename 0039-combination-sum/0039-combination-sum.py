class Solution:
    def combinationSum(self, cans: List[int], target: int) -> List[List[int]]:
      res = []
      combs = []
      
      def dfs(i, curr):
        
        if curr == target:
          res.append(combs[:])
          return
        
        if curr > target or i >= len(cans):
          return
        
        #to include
        combs.append(cans[i])
        dfs(i, curr + cans[i])
        
        #to not include
        combs.pop()
        dfs(i + 1, curr)
        
      dfs(0, 0)
      
      return res
      
        