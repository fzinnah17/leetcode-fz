class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 1:
        return [[], [nums[0]]]
      
      nums.sort()
      res = set()
      subset = []
      
      def dfs(i):
          
        #base case
        if i == len(nums):
          res.add(tuple(subset))
          return
        
        #include
        subset.append(nums[i])
        dfs(i + 1)
        
        #don't include
        subset.pop()
        dfs(i + 1)
        
      dfs(0)
      return res