class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        cans = []
        
        def dfs(i, curr_sum):
            
            if curr_sum == target:
                res.add(tuple(cans[:]))
                return
            
            if i >= len(nums) or curr_sum > target:
                return
            
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                cans.append(nums[j])
                dfs(j + 1, curr_sum + nums[j])
                
                cans.pop()
                # dfs(j + 1, curr_sum)
                
        dfs(0, 0)
        return res