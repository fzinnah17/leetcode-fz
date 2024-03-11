class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def dfs(i, curr):
            if i == len(curr):
                binary_str = ''.join(curr)
                if binary_str not in nums:
                    return binary_str
            
            if i >= len(curr):
                return
            
            curr[i] = '0'
            result = dfs(i + 1, curr)
            if result:
                return result
            
            curr[i] = '1'
            result = dfs(i + 1, curr)
            if result:
                return result
            
            curr[i] = '0'  # Backtrack
            return None
        
        n = len(nums[0])
        initial = ['0'] * n
        return dfs(0, initial)
