class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []        
        def dfs(path, remaining):
            if not remaining:
                res.append(path)
                return
            
            for _ in range(len(remaining)):
                element = remaining.pop(0)
                dfs(path + [element], remaining)
                remaining.append(element)
            
        dfs([], nums)
        return res
        
        