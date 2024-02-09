class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 1:
        return [[], [nums[0]]]
      
      res = []
      subset = []
      
      def dfs(i):
        #base case
        if i == len(nums):
          res.append(subset[:]) #subset's copy is added
          return
        
        #to include the number
        subset.append(nums[i])
        dfs(i + 1)
        
        # or to not include the number
        subset.pop()
        dfs(i + 1)
        
      dfs(0)
      
      return res