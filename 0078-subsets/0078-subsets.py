class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        to include
        to not include
        """
        res = []
        subs = []
        
        def dfs(i):
          
          if i == len(nums):
            res.append(subs[:])
            return
          
          subs.append(nums[i])
          dfs(i+1)
          subs.pop()
          dfs(i+1)
        dfs(0)
        return res
      