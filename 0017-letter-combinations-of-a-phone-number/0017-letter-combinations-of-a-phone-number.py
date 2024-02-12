class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      """
      just like permutations
      """
      # print(len(digits))
      if not len(digits):
        return []
      numMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
      }

      if len(digits) == 1:
        return list(numMap[digits])
        # return all the characters mapped to that number        
        
      res = []
      permutations = []
      
      def dfs(i):
        
        if i >= len(digits):
          res.append("".join(permutations))
          return
        
        #append and then call the dfs function
        #pop and then call the dfs function
        for ch in numMap[digits[i]]:
          permutations.append(ch)
          dfs(i + 1)
          permutations.pop()
        
        
      dfs(0)
      
      return res
      