class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        combs = []
        candidates.sort()
        
        def dfs(i, curr):
            
            if curr == target:
                res.add(tuple(combs))
                return
            
            if i >= len(candidates) or curr > target:
                return
            
            for k in range(i, len(candidates)):
                if k > i and candidates[k] == candidates[k - 1]:
                    continue
                combs.append(candidates[k])
                dfs(k + 1, curr + candidates[k])
            
                combs.pop()            
            
        dfs(0, 0)
        
        return res