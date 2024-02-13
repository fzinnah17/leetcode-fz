class Solution:
    def splitString(self, s: str) -> bool:
        # Helper function for DFS search
        def dfs(index, prev):
            # If we've reached the end of the string successfully, return True
            if index == len(s):
                return True
            
            # Try every possible split of the remaining string
            for end in range(index + 1, len(s) + 1):
                num = int(s[index:end])
                
                # If no previous number is set or if the current number is exactly one less than the previous
                if prev is None:
                    # Skip the entire string being converted into one number
                    if len(s) == end:
                        continue
                    if dfs(end, num):
                        return True
                elif num + 1 == prev:
                    if dfs(end, num):
                        return True
                    
            return False
        
        return dfs(0, None)
