class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      """
      decision tree:
        1. take the target - curr num
        7 - 2 = 5
        2. check if the subtraction is there or not
        3. if not then either use the same value or go to the next value
             2                  3              6             7
         /  /  \  \            / \            / \           / \
         
          """
      res = []
      combinations = []

      def dfs(i, curr):
        if curr == target:
          res.append(combinations[:])
          return
        if i >= len(candidates) or curr > target:
          return

          # Choose the current number and continue with the same number
        combinations.append(candidates[i])
        dfs(i, curr + candidates[i])
        combinations.pop()  # Remove the last number

        # Skip the current number and move to the next one
        dfs(i + 1, curr)

      dfs(0, 0)
      return res
