class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
        combination = []

        def dfs(i):
            nonlocal res
            
            if i >= len(arr):
                concatenated = ''.join(combination)
                if len(set(concatenated)) == len(concatenated):
                    res = max(res, len(concatenated))
                return
            
            combination.append(arr[i])
            dfs(i + 1)
            
            combination.pop()
            dfs(i + 1)

        dfs(0)
        return res
