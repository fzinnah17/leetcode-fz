class Solution(object):
    def rob(self, nums):
        """
Pseudocode:
1. Create a memory table to remember the calculated results for each house
        Helper Function:
        (
        2. If we have already calculated the result for this house, just return it from memory
        3. If the house_index is greater than or equal to the total number of houses, that means we have considered all houses and cannot rob anymore, so we return 0 because we can't rob anything.
        4. Now, we have two options: 
                either rob the current house and skip the next one,
                or skip the current house and rob the next one.
        5. We will choose the option that gives us the maximum amount of money and store it in memory
        6. Return the maximum amount for the current house
        )
7. Start the recursion from the first house and return the max money outside of the helper function
TC: O(N), where N is the number of houses. This is because the function dfs(currH) is called for each house once, and in each call, we either explore two possible scenarios (dfs(currH + 1) and dfs(currH + 2)) or retrieve the value from the memoization dictionary memo.

SC: O(N), where N is the number of houses. This is because the memoTable dictionary is used to store the results of subproblems, and its size grows with the number of houses. In the worst case, it can store the results for all houses.

        """
        memoTable = {} #index/key : current house robbing  value: amount aka nums[i]
        def dfs(currHouse):
            if currHouse in memoTable:
                return memoTable[currHouse]
            if currHouse >= len(nums): #we cant rob anymore after visitng the houses to rob
                return 0
            robHere = nums[currHouse] + dfs(currHouse + 2) #one possibility: we are robbing the current house and the second house after the current house to not trigger the police alarm

            robNext = dfs(currHouse + 1) #second possibility: we are skipping the current house and moving on to the next one because we think that might give us more money
            
            memoTable[currHouse] = max(robHere, robNext) #choose which possibility is better
            
            return memoTable[currHouse]
        
        return dfs(0)
            
                
        