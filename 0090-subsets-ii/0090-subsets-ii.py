class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        nums.sort()
        
        def dfs(i):
            if i >= len(nums):
                res.add(tuple(curr[:]))
                return
            
            curr.append(nums[i])
            dfs(i+1)
            
            curr.pop()
            dfs(i + 1)
        dfs(0)
        return res
        
        