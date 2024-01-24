class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      """
      [2,3,4,5]
      first ques how many subsets will be there? 2^n
      output = [[], [2], [3], [4], [5], [2,3], [2,4], [2,5], [2,3,4], [2,3,5], [2,4,5], [2,3,4,5], [3,4], [3,5], [3,4,5], [4,5]]
      """
      res = []
      
      subset = [] #allocate an array that can give global access to the helper function
      
      #i is the index of the value we are making the decision on
      def dfs(i):
        #if we finished iterating the array then we know we can add it to the result list
        if i >= len(nums):
          res.append(subset[:]) #[:] or copy() because subset will be modified in each level of the decision tree
          return
        
        #we choose the path
        subset.append(nums[i])
        dfs(i + 1) #this has the new element we are adding
        
        #we do not choose the path means 
        subset.pop() #this is for the empty subset
        dfs(i + 1)
      dfs(0)
      return res