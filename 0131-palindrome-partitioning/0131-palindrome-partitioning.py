class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s[0]]]
        res = []
        parts = []
            
        def isPalindrome(s, left, right):
            #we will use a two pointers approach
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(parts[:])
                return
            for j in range(i, len(s)):
               #call the helper function
               if isPalindrome(s, i, j):
                    parts.append((s[i:j + 1]))
                    dfs(j + 1)

                    #backtrack
                    parts.pop()
        dfs(0)
        return res
        