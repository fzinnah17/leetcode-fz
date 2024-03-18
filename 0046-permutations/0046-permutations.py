class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perms = []
        
        def dfs(i):
            if i >= len(nums):
                res.append(perms[:])
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                perms.append(nums[i])
                dfs(i+1)
                perms.pop()
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res
        