class Solution:
    def permute(self, nums):
        res = []
        
        def dfs(path, options):
            if not options:  # When no options left, we found a permutation
                res.append(path)
                return
            
            for _ in range(len(options)):
                el = options.pop(0)  # Pop from start (modify to pop from end if desired)
                dfs(path + [el], options)
                options.append(el)  # Append back to restore the list for the next iteration
        
        dfs([], nums)  # Start DFS with an empty path and nums as the initial options list
        
        return res
