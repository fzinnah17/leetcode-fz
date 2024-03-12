class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        curr_str = []
        num_set = set(nums)
        
        def dfs(i):
            nonlocal res
            if res:
                return
            
            
            if i == len(nums[0]):
                candidate = ''.join(curr_str)
                # print(f"checking candidate: {candidate}")
                if candidate not in num_set:
                    res = candidate
                    return
                
            if res:
                return
            if i < len(nums[0]):     
                curr_str.append("0")
                dfs(i + 1)
                curr_str.pop()

                if res:
                    return

                curr_str.append("1")
                dfs(i + 1)
                curr_str.pop()
        
        dfs(0)
        return res
        
    
    