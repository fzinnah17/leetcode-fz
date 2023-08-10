class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        
        1. table = {}
        leetcode
        c
           i
        """
        memoTable = {}
        def helper(curr):
            if curr == len(s):
                return True
            if curr in memoTable:
                return memoTable[curr]
            for word in wordDict:
                #leet code
                #        c
                if s[curr:curr+len(word)] == word and helper(curr+len(word)):
                    memoTable[curr] = True
                    return memoTable[curr]
            memoTable[curr] = False
            return False
        return helper(0)
        