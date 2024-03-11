class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def dfs(i):
            if i == n:
                binary_str = ''.join(curr)
                if binary_str not in nums:
                    return binary_str
            
            if i >= n:
                return
            
            curr.append('0')
            result = dfs(i + 1)
            if result:
                return result
            curr.pop()
            
            curr.append('1')
            result = dfs(i + 1)
            if result:
                return result
            curr.pop()
            
            return None
        
        n = len(nums[0])
        curr = []
        return dfs(0)
