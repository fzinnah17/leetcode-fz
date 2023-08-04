"""
Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to produce a sum of money x using the available coins in such a way that the number of coins is minimal.

For example, if the coins are {1,5,7} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.

Input: The first input line has two integers n and x : the number of coins and the desired sum of money.
The second line has n distinct integers c1,c2,…,cn: the value of each coin.

Input: n = 3, x = 11, coins = [1, 5, 7]
Output: 3 (Explanation: An optimal solution is 5 + 5 + 1, which requires 3 coins.)

Input: n = 4, x = 9, coins = [2, 3, 5, 6]
Output: 2 (Explanation: An optimal solution is 3 + 6, which requires 2 coins.)

Input: n = 2, x = 10, coins = [1, 9]
Output: 2 (Explanation: An optimal solution is 9 + 1, which requires 2 coins.)

Input: n = 5, x = 15, coins = [1, 2, 3, 4, 5]
Output: 3 (Explanation: An optimal solution is 5 + 5 + 5, which requires 3 coins.)

Input: n = 3, x = 16, coins = [2, 8, 10]
Output: 2 (Explanation: An optimal solution is 8 + 8, which requires 2 coins.)

Input: n = 4, x = 14, coins = [3, 5, 7, 11]
Output: 2 (Explanation: An optimal solution is 7 + 7, which requires 2 coins.)

Input: n = 6, x = 26, coins = [1, 3, 7, 9, 15, 10]
Output: 3 (Explanation: An optimal solution is 7 + 9 + 10, which requires 3 coins.)

State/Subproblem: For the current ith coin, dp[i] = minimum number of coins to make sum of i      [[[[making it 'x' here means solving the big problem, but we are focusing on the smaller problem]]]]

Transition/Formula: for each k value in the array, we find the minimum number of ways: [10,5,6,11]
                    dp[i] = min(dp[n-coins[i]+1)
                    dp[i] = {min(dp[n-10],dp[n-5],dp[n-6],dp[n-11]) + 1}

TC: #of states * transition time = O(x * n)
SC: O(x) = #of states/subproblems
"""

def minCoins(n,x,coins):
  memoTable = [float("inf")] * (x + 1)
  memoTable[0] = 0
  def helper(currSum):
    if currSum == 0:
      return 0
    if memoTable[currSum] != float("inf"):
      return memoTable[currSum]
    for i in coins:
      if currSum - i >= 0:
        memoTable[currSum] = min(memoTable[currSum], helper(currSum - i) + 1)
    return memoTable[currSum]
  helper(x)
  return memoTable[x]
    
    
