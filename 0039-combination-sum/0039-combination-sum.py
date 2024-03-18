class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cans = []
        
        def dfs(i, curr):
            if curr == target:
                res.append(cans[:])
                return
            
            if i >= len(nums) or curr > target:
                return
            
            for j in range(i, len(nums)):
                 
                #to include
                cans.append(nums[j])
                dfs(j, curr + nums[j]) #to allow the same number be used multiple times
                # dfs(j + 1, curr + nums[j]) only if we were only finding the target not what we are looking up
                #to not include
                cans.pop()
                # dfs(j + 1, curr) do not use it because we can use same number multiple times
                
        dfs(0, 0)
        return res
        
        