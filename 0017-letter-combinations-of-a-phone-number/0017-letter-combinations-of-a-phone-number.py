class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        #key = number and value = letters
        numMap = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
        if not s:
            return []
        if len(s) == 1:
            return list(numMap[s])

        res = []
        combs = []

        def dfs(i):
            if i >= len(s):
                res.append(''.join(combs)) 
                return

            # for j in range(i, len(s)):
                #map the j with the hashmap
                #take the hashmap values and make the combinations
            for char in numMap[s[i]]:
                combs.append(char)
                dfs(i + 1)
                combs.pop()

        dfs(0)
        return res
