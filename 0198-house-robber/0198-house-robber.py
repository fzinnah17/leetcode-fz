class Solution(object):
    def rob(self, nums):
        """
        state/subproblem: maximum amount of money gained from 0 to the current ith value such that we are never picking adjacent elements
        transition/choices:
            1. pick the current house and can't pick the prev or next house
                nums[i] + dp[i-2]
            2. don't pick the current house and allowed to pick prev or next house
                dp[i-1]
        TC: O(nlogn) SC: O(nlogn)
        pattern is if we find the value then we return memo[i]
        as we are calculating the function to find max/min, assign that value to the same memo[i]
        return that memo[i]
        """
        memoTable = {}
        def dp(currHouse):
            if currHouse >= len(nums):
                return 0
            if currHouse in memoTable:
                return memoTable[currHouse]
            pickCurr = nums[currHouse] + dp(currHouse + 2)
            dontCurr = dp(currHouse + 1)
            memoTable[currHouse] = max(pickCurr, dontCurr)
            return memoTable[currHouse]
        return dp(0)

"""
if we are starting to rob from the end of the list then boundary needs to be changed to currHouse < 0 and dp has to be starting from len(nums - 1)
        memoTable = {}
        def dp(currHouse):
            if currHouse < 0:
                return 0
            if currHouse in memoTable:
                return memoTable[currHouse]
            pickCurr = nums[currHouse] + dp(currHouse - 2)
            dontCurr = dp(currHouse - 1)
            memoTable[currHouse] = max(pickCurr, dontCurr)
            return memoTable[currHouse]
        return dp(len(nums)-1)"""
            
        