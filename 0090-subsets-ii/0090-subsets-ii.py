class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 1:
        return [[], [nums[0]]]
      nums.sort()
      res = set()
      subsets = []
      
      def dfs(i):
        if i >= len(nums):
          res.add(tuple(subsets[:]))
          return
        
        subsets.append(nums[i])
        dfs(i + 1)
        
        subsets.pop()
        dfs(i + 1)
        
      dfs(0)
      return res
      
        