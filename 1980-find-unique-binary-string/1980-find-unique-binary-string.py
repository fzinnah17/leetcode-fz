class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Use a set for faster lookup
        # once a valid binary string (not in num_set) is found, stop the recursion.
        # Don't explore further after finding a valid string.
        num_set = set(nums)
        res = ""
        curr_str = []
        
        def dfs(i):
            nonlocal res
            if i == len(nums[0]):
                candidate = ''.join(curr_str)
                if candidate not in num_set:
                    res = candidate
                    return True
                return False
            # Only continue recursion if we haven't found a result   
            if not res:
                curr_str.append("0")
                if dfs(i + 1):
                    return True
                curr_str.pop()
            
            if not res:
                curr_str.append("1")
                if dfs(i + 1):
                    return True
                curr_str.pop()
            return False
            
        dfs(0)
        return res

#         def dfs(i):
#             nonlocal res
#             if i == len(nums[0]):
#                 candidate = ''.join(curr_str)
#                 if candidate not in num_set:
#                     res = candidate
#                     return True
#                 return False

#             # Try with '0'
#             curr_str.append('0')
#             if dfs(i + 1):
#                 return True
#             curr_str.pop()

#             # Try with '1'
#             curr_str.append('1')
#             if dfs(i + 1):
#                 return True
#             curr_str.pop()

#             return False

#         dfs(0)
#         return res
