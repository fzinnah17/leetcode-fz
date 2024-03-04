class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 1:
        return [[], [nums[0]]]
      nums.sort()
      res = []
      subsets = []
      
      def dfs(i):
        if i >= len(nums):
          res.append(subsets[:])
          return
        
        subsets.append(nums[i])
        dfs(i + 1)
        
        subsets.pop()
        # Skip all duplicates of the current element
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
              
        dfs(i + 1)
        
      dfs(0)
      return res
      
        