class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
      """
      we have an array
      pop one element
      do the dfs on it
      append it from the end
      and do the dfs again
      repeat the process until the last element of the array is reached
      """
      res = []
      
      #base case:
      if len(nums) == 1:
        return [[nums[0]]]
      
      def dfs(path, remNums):
        # if no elements left from the nums array then just add it to the result
        if not remNums:
          res.append(path)
          return
        
        # we iterate over each of the array on each step to remove and add it back
        for _ in range(len(remNums)):
          el = remNums.pop(0)
          dfs(path + [el], remNums)
          remNums.append(el)

      dfs([], nums)
      
      return res