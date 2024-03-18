class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        perms = []
        
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(perms[:]))
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                nums[i], nums[j] = nums[j], nums[i]
                perms.append(nums[i])
                dfs(i + 1)
                perms.pop()
                # dfs(i + 1)
                nums[i], nums[j] = nums[j], nums[i]
        dfs(0)
        return res