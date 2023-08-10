class Solution(object):
    def wordBreak(self, s, wordDict):
        
        memoTable = {}
        def helper(curr):
            if curr == len(s):
                return True
            if curr in memoTable:
                return memoTable[curr]
            for i in range(curr + 1, len(s) + 1):
                if s[curr:i] in wordDict and helper(i):
                    memoTable[curr] = True
                    return True
            memoTable[curr] = False
            return False
      
        return helper(0)
        