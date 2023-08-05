"""
Consider a money system consisting of n coins. Each coin has a positive integer value. Your task is to calculate the number of distinct ways you can produce a money sum x using the available coins.

For example, if the coins are n = {2,3,5}, and the desired sum is x = 9, there are 8 ways:
2+2+5
2+5+2
5+2+2
3+3+3
2+2+2+3
2+2+3+2
2+3+2+2
3+2+2+2

State/Subproblem: for the ith value, dp[i] = the distinct number of ways to calculate the ith value using n coins.
Transition/Formula: dp[i] = sum(dp[i-k])

Pseducodoe:
x - n = ans, check if 'ans' is in the n coin set, if not then, do 'ans' - n 
                    as long as the ans = 0, count += 1
n1 = 3
x1 = 11
coins1 = [1, 5, 7]
Output: 3

n2 = 2
x2 = 6
coins2 = [2, 3]
Output: 2

n3 = 4
x3 = 9
coins3 = [2, 3, 5, 7]
Output: 3

n4 = 4
x4 = 12
coins4 = [2, 3, 5, 7]
Output: 5

n5 = 5
x5 = 14
coins5 = [1, 3, 5, 7, 9]
Output: 4

n6 = 6
x6 = 20
coins6 = [4, 6, 10, 12, 15, 18]
Output: 2

TC: #of states * #of transition = O(x * n)
SC: O(x) = #of states/subproblems
"""

def coinCombo(n,x,coins):
  memoTable = [0] * (x + 1) 
  memoTable[0] = 1 """currSum = 0 return 0 not picking any coins means I am having a choice here"""
  def dp(currSum):
    if currSum == 0:
      return 1
    if memoTable[currSum] != 0:
      return memoTable[currSum]
      
    for i in coins:
      if currSum - i >= 0:
        memoTable[currSum] += dp[currSum - i]
    return memoTable[currSum]
  dp(x)  
  return memoTable[x] """function's scope"""
      
    
