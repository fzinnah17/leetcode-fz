class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      if len(nums) == 1:
        return [[nums[0]]]
      
      res = set()
      
      def dfs(path, remNums):
        
        #all the permuations are found and we reached the last element
        if not remNums:
          res.add(tuple(path))
          return
      
        for _ in range(len(remNums)):
          el = remNums.pop(0) #pop from the left
          # print(f"popped element: {el}")
          # print()
          dfs(path + [el], remNums)
          # print(f"path with popped element: {path + [el]}")
          # print()
          remNums.append(el)
          # print(path)
        # print(f"res: {res}")
      dfs([], nums)
      
      return res