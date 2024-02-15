class Solution:
    def combinationSum2(self, cans: List[int], target: int) -> List[List[int]]:
      
      res = set()
      combs = []
      cans.sort()
      # print(cans) [1, 1, 1, 1, 2, 2, 3, 4, 4, 5, 5]
      
      
      def dfs(i, curr):
        
        if curr == target:
          res.add(tuple(combs))
          return
        
        if i >= len(cans) or curr > target:
          return
        for k in range(i, len(cans)):
          if k > i and cans[k] == cans[k-1]:
            continue
          combs.append(cans[k])
          dfs(k + 1, curr+ cans[k])

          combs.pop()
          # dfs(k + 1, curr)
        
      dfs(0, 0)
      
      return res
          
        