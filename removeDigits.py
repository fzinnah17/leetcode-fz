"""
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?

State/Subproblem: For integer i, the number of steps to make it to 0 dp[i] = min number of steps to make i == 0
Transition/Formula: dp[i] = min(different i - remaineder(i) if remainder(i) > 0) + 1 ; { + 1 to take a step, removing a digit: performing an operation}
base case: dp[0] = 0
final subproblem: dp[n]
"""

def removeDigits(n):
  memoTable = [0] * (n + 1)
  def helper(currNum):
    if currNum <= 0:
      return 0
    if memoTable[currNum] != 0:
      return memoTable[currNum]
    for i in range(len(currNum):
      memoTable[currNum] += min(currNum - (currNum % 10 if currNum % 10 > 0)) + 1
    return memoTable[currNum]
  return helper(n)
